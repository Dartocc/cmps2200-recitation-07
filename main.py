from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop()
        for neighbor in graph[node]:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result


def connected(graph):
    ### TODO
    if not graph:
        return True
    start_node = next(iter(graph))
    reached = reachable(graph, start_node)
    return len(reached) == len(graph)


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    unvisited = set(graph.keys())
    count = 0
    while unvisited:
        start = unvisited.pop()
        component = reachable(graph, start)
        unvisited -= component
        count += 1
    return count
