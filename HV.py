from graph import Graph
from drawer import Drawer

# returns map {id: (int, int)}
def HV(graph: Graph, root: int, x_shift: int = 0):
    result = drawDfs(graph, root)
    # rotate 45
    #return {k: (v[0] + x_shift, v[0] + v[1] + 10) for k, v in result.items()}
    return {k: (v[0] + x_shift, v[1] + 10) for k, v in result.items()}


def shift_coords(m: map, shift: tuple):
    return {k: (v[0] + shift[0], v[1] + shift[1]) for k, v in m.items()}


def drawDfs(graph: Graph, v: int):
    result = {
        v: (0, 0)
    }
    left, right = None, None
    negs = graph.get_negs(v)
    assert len(negs) <= 2
    if len(negs) == 0:
        return result
    left = drawDfs(graph, negs[0])
    result = {**result, **shift_coords(left, (0, 20))}
    if len(negs) == 2:
        right = drawDfs(graph, negs[1])
        x_shift = max(map(lambda x: x[0], left.values())) + 20
        result = {**result, **shift_coords(right, (x_shift, 0))}

    return result
