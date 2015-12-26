#!/usr/bin/env python

import json
import argparse
import xml.etree.ElementTree as ET
from collections import OrderedDict


# global variables
PREFIX = '{http://graphml.graphdrawing.org/xmlns/graphml}'
GRAPHML = dict(
    key   = PREFIX + 'key',
    graph = PREFIX + 'graph',
    node  = PREFIX + 'node',
    edge  = PREFIX + 'edge',
    data  = PREFIX + 'data'
    )

def extract_edges(edges):
    '''get all edge data'''
    edge_list = []
    for edge in edges:
        attr = edge.attrib
        attr_dict = OrderedDict((
                ('id',     attr['id']),
                ('source', attr['source']),
                ('target', attr['target'])
                ))
        edge_list.append(attr_dict)
    return edge_list

def get_node_data(node):
    '''extract data from single node'''
    data = node.find(GRAPHML['data']).find('hmcnode').attrib
    gdict = OrderedDict()
    gdict['id']     = data['id']
    gdict['labels'] = [dict(text=gdict['id'])]
    gdict['width']  = 10
    gdict['height'] = 10
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

def convert2json(filename):
    '''convert all node and edge data into a single object'''
    # parse xml data
    tree  = ET.parse(filename)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command line utility to convert Harris Matrix Composer-GraphML file to JSON')
    parser.add_argument(
        'filename',
        metavar='filename',
        type=str,
        help='XML (HMC-GraphML) file to convert'
        )
    parser.add_argument(
        'outfile',
        metavar='outfile',
        type=str,
        help='Filename to save as JSON'
        )
    args = parser.parse_args()

    json_data = convert2json(args.filename)

    with open(args.outfile, 'w') as outfile:
        json.dump(json_data, outfile, indent=2)
