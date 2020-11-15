from graph import Graph

def strongly_connected_components(graph):
    '''
    params:
        - graph: dict of { node: list of connected nodes }

    output:
        - sorted_nodes: sorted node
    '''
    graph_obj = Graph(graph)
    graph_obj.dfs()
    trans_graph = graph_obj._transpose()
    trans_graph_obj = Graph(trans_graph)
    print("checking strongly connected components")
    scc = trans_graph_obj.scc_detect()
    print(scc)
