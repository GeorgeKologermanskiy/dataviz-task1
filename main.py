import argparse
import os
from graph import Graph
from drawer import Drawer
from HV import HV


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str, help='Input graphml file')
    parser.add_argument('-o', '--output', required=True, type=str, help='Output .svg file')
    return parser.parse_args()


def main():
    args = parse_args()
    input_file = args.input
    output_file = args.output

    if not os.path.isfile(input_file):
        print(input_file, 'is not a regular file')
        return

    # parse graph from file
    graph = Graph(input_file)
    # create drawer
    drawer = Drawer()
    x_shift = 10
    for root in graph.get_roots():
        node_coords = HV(graph, root, x_shift)
        for node, coords in node_coords.items():
            for to in graph.get_negs(node):
                drawer.add_edge(coords, node_coords[to])
        x_shift = max(map(lambda x: x[0], node_coords.values())) + 20 * 2

    # save as svg file
    drawer.saveSvg(output_file)


if __name__ == '__main__':
    main()