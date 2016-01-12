# Harris Matrix Visualization

## Converting Harris Matrix Composer XML

The command line utility `hmc2json.py`, written in Python 3.5, will convert Harris Matrix Composer-style GraphML data to [JSON Graph Format](https://rtsys.informatik.uni-kiel.de/confluence/display/KIELER/JSON+Graph+Format).

Data exported from Harris Matrix Composer is packaged as a zip file with two XML documents: `project.xml` and `matrix.xml`. The latter contains the necessary graph data.

```sh
$ unzip matrix.hmcx
$ ./hmc2json.py matrix.xml matrix.json
```

## Visualization

[KLayJS-D3](https://github.com/OpenKieler/klayjs-d3) is the main workhorse of these visualizations. The library provides a hierarchical, orthogonal graph layout algorithm that determines node placement and edge routing.

### Examples

- [Demo](https://semerj.github.io/harris-matrix/examples/demo/)
- [Sector D](https://semerj.github.io/harris-matrix/examples/Sector_D/)
- [PEA](https://semerj.github.io/harris-matrix/examples/PEA/)
- [A2](https://semerj.github.io/harris-matrix/examples/A2/)

### Installation

To view the visualization, first install the required JS libraries ([D3](https://github.com/mbostock/d3), [KLayJS](https://github.com/OpenKieler/klayjs), and [KLayJS-D3](https://github.com/OpenKieler/klayjs-d3)) with a single command:

```sh
$ bower install klayjs-d3
```
