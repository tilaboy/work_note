from graph import Graph, strongly_connected_components

g_22_6 = {
    'q': ['s', 't', 'w'],
    'r': ['u', 'y'],
    's': ['v'],
    't': ['y', 'x'],
    'u': ['y'],
    'v': ['w'],
    'w': ['s'],
    'x': ['z'],
    'y': ['q'],
    'z': ['x']
}


g_22_8 = {
    'm': ['q', 'r', 'x'],
    'n': ['o', 'q', 'u'],
    'o': ['r', 's', 'v'],
    'p': ['o', 's', 'z'],
    'q': ['t'],
    'r': ['u', 'y'],
    's': ['r'],
    't': [],
    'u': ['t'],
    'v': ['w', 'x'],
    'w': ['z'],
    'x': [],
    'y': ['v'],
    'z': []
}

graph_22_6 = Graph(g_22_6)
graph_22_8 = Graph(g_22_8)

#print(graph_22_8)
#graph_22_8.bfs()
#graph_22_8.dfs()
#graph_22_8.shortest_path_find('m', 'z')
degree_sorted = graph_22_8.top_sort_zero_degree()
print('degree sort', [node.val for node in degree_sorted])

sorted = graph_22_8.top_sort()
print('dfs sort', [node.val for node in sorted])

#for node in sorted:
#    print("val:{}, par:{}, {} -> {}".format(node.val,
#                                            node.pi.val if node.pi else 'None',
#                                            node.d,
#                                            node.f))

path_pv = graph_22_8.find_all_path('p', 'v')
print('from p to v:', path_pv)
path_pz = graph_22_8.find_all_path('p', 'z')
print('from p to z:', path_pz)
path_rx = graph_22_8.find_all_path('r', 'x')
print('from r to x:', path_rx)
graph_22_6.dfs()

strongly_connected_components(g_22_8)
