# Harris Matrix Visualization

## Converting Harris Matrix Composer XML

The command line utility `hmc2json.py`, written in Python 3.5, will convert a Harris Matrix Composer-style GraphML data to [JSON Graph Format](https://rtsys.informatik.uni-kiel.de/confluence/display/KIELER/JSON+Graph+Format). 

Harris Matrix Composer data is exported as a zipped file, which typically contains two `xml` documents: `project.xml` and `matrix.xml`. The latter contains the necessary graph data.

```sh
$ ./hmc2json.py matrix.xml matrix.json
```

## Visualization

[KLayJS-D3](https://github.com/OpenKieler/klayjs-d3) is the main workhorse of these visualizations. The library provides a hierarchical, orthogonal graph layout algorithm that determines node placement and edge routing.

### Examples

- [Sector D](https://semerj.github.io/harris-matrix/examples/Sector_D/)
- [PEA](https://semerj.github.io/harris-matrix/examples/PEA/)
- [A2](https://semerj.github.io/harris-matrix/examples/A2/)

### Installation

To view the visualization, first install the required JS libraries ([D3](https://github.com/mbostock/d3), [KLayJS](https://github.com/OpenKieler/klayjs), and [KLayJS-D3](https://github.com/OpenKieler/klayjs-d3)) with a single command:

```sh
$ bower install klayjs-d3
```

### Differences with Harris Matrix Composer

KLayJS-D3 [does *not* support](http://rtsys.informatik.uni-kiel.de/confluence/questions/14516313/can-klaylayered-consider-previous-node-coordinates#Layering) `"CONTEMPORARY"` (i.e. bidirectional) edges as in Harris Matrix Composer. Example:

![img 1](contemporary.png)

Instead, these visualizations provide undirected, dashed, and colored edges to signify `"CONTEMPORARY"` relationships between nodes. Example:

![img 2](contemporary2.png)
