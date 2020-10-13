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

g_22_8 = {
    'm': ['q', 'r', 'x'],
    'n': ['o', 'q', 'u'],
    'o': ['r', 's'],
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

visited = [False] * n


class Vertex:
    def __init__(self, val):
        self.color = 'w'
        self.d = 0
        self.pi = None
        self.f = 0
        self.val = val
        self.edges = list()

    def update_edges(self, edges, vertices):
        self.edges = [vertices[e] for e in edges]

    def __str__(self):
        parent = self.pi.val if self.pi else None
        return 'v:{}\tpi:{}\td:{}\tc:{}'.format(self.val, parent, self.d, self.color)

def initialize_graph(graph):
    vertices = {v:Vertex(v) for v in graph}
    for vertex in vertices:
        vertices[vertex].update_edges(graph[vertex], vertices)
    return vertices


def bfs_color(vertices, seed):
    seed_v = vertices[seed]
    seed_v.color = 'g'
    queue = [seed_v]
    while queue:
        u = queue.pop(0)
        for vertex in u.edges:
            if vertex.color == 'w':
                vertex.color = 'g'
                vertex.d = u.d + 1
                vertex.pi = u
                queue.append(vertex)
        u.color = 'b'


def shortest_path_print(source, target):
    if source.val == target.val:
        print(source.val)
    elif target.pi is None:
        print('no available path')
    else:
        shortest_path_print(source, target.pi)
        print(target.val)



vertices = initialize_graph(g)
bfs_color(vertices, 0)
for vertex in vertices:
    print(vertex, vertices[vertex])
shortest_path_print(vertices[0], vertices[4])




def bfs(at, visited, sub_graph, graph):
    visited[at] = True
    neighbours = graph[at]
    for vertex in neighbours:
        if visited[vertex] == False:
            pass

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
