n = 13
g = {
    0: [9, 1],
    1: [8],
    2: [],
    3: [2, 4, 5],
    4: [],
    5: [6],
    6: [7],
    7: [10, 3, 6],
    8: [7],
    9: [8],
    10: [11],
    11: [12],
    12: [],

}
visited = [False] * n

def dfs(at, visited, sub_graph, graph):
    visited[at] = True
    neighbours = graph[at]
    for next in neighbours:
        if visited[next] == False:
            dfs(next, visited, sub_graph, graph)
    sub_graph.append(at)

def top_sort(graph):
    nr_node = len(graph)
    visited = [False] * nr_node
    sorted_node = [0] * nr_node
    i = nr_node - 1

    for at in range(nr_node):
        if visited[at] == False:
            sub_graph = []
            dfs(at, visited, sub_graph, graph)
            for node in sub_graph:
                sorted_node[i] = node
                i = i - 1
    return sorted_node


print(top_sort(g))
