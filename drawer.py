import drawSvg as draw

class Drawer:

    def __init__(self):
        self.nodes_coords = set()
        self.edges_coords = []

    def add_edge(self, node1: tuple, node2: tuple):
        self.nodes_coords.add(node1)
        self.nodes_coords.add(node2)
        self.edges_coords.append((node1, node2))
    
    def saveSvg(self, output_file: str):
        # calculate sizes
        x_limit = int(max(map(lambda x: x[0], self.nodes_coords)) + 20)
        y_limit = int(max(map(lambda x: x[1], self.nodes_coords)) + 20)
        d = draw.Drawing(x_limit, y_limit)
        # draw edges
        for edge in self.edges_coords:
            a, b = edge
            l = draw.Lines(
                a[0], y_limit - a[1],
                b[0], y_limit - b[1],
                close=False,
                fill='#eeee00',
                stroke='black')
            d.append(l)
        # draw vertexes
        r = min(map(lambda v: (v[0][0] - v[1][0])**2 + (v[0][1] - v[1][1])**2,
                    self.edges_coords))
        r = min(r / 3, 5)
        for (x, y) in self.nodes_coords:
            #x, y = node
            circle = draw.Circle(x, y_limit - y, r, fill='red')
            d.append(circle)
        # save to file
        d.saveSvg(output_file)