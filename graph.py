from pygraphml import GraphMLParser

class Graph:

    def __init__(self, input_file: str):
        graph = GraphMLParser().parse(input_file)
        nodes_mapping = {}
        self.roots = set()
        # parse vertexes
        for node in graph.nodes():
            id = node.id
            nodes_mapping[id] = len(nodes_mapping)
            self.roots.add(nodes_mapping[id])
        self.size = len(nodes_mapping)
        self.edges = [[] for _ in range(self.size)]
        # parse edges
        for edge in graph.edges():
            num1 = nodes_mapping[edge.node1.id]
            num2 = nodes_mapping[edge.node2.id]
            self.edges[num1].append(num2)
            self.roots.remove(num2)
        self.roots = list(self.roots)
        assert len(self.roots) > 0

    def get_size(self):
        return self.size

    def get_roots(self):
        return self.roots

    def get_negs(self, v: int):
        return self.edges[v]
