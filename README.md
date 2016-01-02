# Harris Matrix Visualization

## Converting Harris Matrix Composor XML

The command line utility `hmc2json.py`, wrriten in Python 3.5, will convert a HMC-style GraphML file to JSON like so:

```sh
$ ./hmc2json.py data.xml data.json
```
## Visualization

[KLayJS-D3](https://github.com/OpenKieler/klayjs-d3) is the main workhorse of these visualizations. The library provides a hierarchical, orthogonal graph layout algorithm that determines node placement and edge routing.

KLayJS-D3 does *not* support `"CONTEMPORARY"` (i.e. bidirectional) edges as in Harris Matrix Composor. Example:

![img 1](contemporary.png)

Instead, these visualizations provide undirected, dashed, and colored edges to signify `"CONTEMPORARY"` relationships between nodes. Example:

![img 2](contemporary2.png)

## Examples

- [Sector D](https://semerj.github.io/examples/sector_d/)
- [PEA](https://semerj.github.io/examples/pea/)
- [A2](https://semerj.github.io/examples/a2/)
