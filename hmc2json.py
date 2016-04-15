#!/usr/bin/env python

import sys
import json
import argparse
import xml.etree.ElementTree as ET
from collections import OrderedDict


# global variables
GRAPHML = dict(
    key   = '{http://graphml.graphdrawing.org/xmlns/graphml}key',
    graph = '{http://graphml.graphdrawing.org/xmlns/graphml}graph',
    node  = '{http://graphml.graphdrawing.org/xmlns/graphml}node',
    edge  = '{http://graphml.graphdrawing.org/xmlns/graphml}edge',
    data  = '{http://graphml.graphdrawing.org/xmlns/graphml}data'
    )


def extract_edges(edges):
    '''get all edge data'''
    edge_list = []
    for edge in edges:
        attr = edge.attrib
        hmcedge = edge.find(GRAPHML['data']).find('hmcedge').attrib
        attr_dict = OrderedDict((
                ('id',     attr['id']),
                ('source', attr['source']),
                ('target', attr['target']),
                ('type',   hmcedge['type'])
                ))
        edge_list.append(attr_dict)
    return edge_list


def get_node_data(node):
    '''extract data from single node'''
    data = node.find(GRAPHML['data']).find('hmcnode').attrib
    gdict = OrderedDict()
    gdict['id']          = data['id']
    gdict['labels']      = [dict(text=gdict['id'])]
    gdict['type']        = data['type']
    gdict['index']       = data['index']
    gdict['name']        = data['name']
    gdict['description'] = data['description']
    gdict['layer']       = data['layer']
    gdict['width']       = 10
    gdict['height']      = 10
    return gdict


def extract_nodes(nodes):
    '''recusively build node tree'''
    node_list = []
    for node in nodes:
        gdict = get_node_data(node)
        gnodes = node.find(GRAPHML['graph'])
        if gnodes:
            gdict['children'] = extract_nodes(
                    gnodes.findall(GRAPHML['node'])
                    )
        node_list.append(gdict)
    return node_list


def xml2json(xml):
    '''convert all node and edge data into a single object'''
    # parse xml data
    tree = ET.fromstring(xml)
    graph = tree.find(GRAPHML['graph'])
    nodes = graph.findall(GRAPHML['node'])
    edges = graph.findall(GRAPHML['edge'])

    # extract node and edge data
    edge_list = extract_edges(edges)
    node_list = extract_nodes(nodes)

    # combine data
    json_data = OrderedDict((
            ('id', 'root'),
            ('children', node_list),
            ('edges', edge_list)
            ))
    return json_data


def parse_arguments():
    '''add parse arguments'''
    parser = argparse.ArgumentParser(
            description='Command line utility to convert \
                         Harris Matrix Composer-GraphML \
                         to JSON')
    parser.add_argument('src', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, help='XML file to convert')
    parser.add_argument('out', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout, help='File to save as JSON')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    json_data = xml2json(args.src.read())
    json.dump(json_data, args.out, indent=2)
