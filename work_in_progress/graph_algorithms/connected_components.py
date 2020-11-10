from graph import Graph


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

graph_22_8 = Graph(g_22_8)
graph_22_8.bfs()
#graph_22_8.dfs()
#graph_22_8.sort_topo()
