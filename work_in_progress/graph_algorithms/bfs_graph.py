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

g_circle = {
    'm': ['q', 'r', 'x'],
    'n': ['o', 'q'],
    'o': ['r', 's'],
    'p': ['o', 's', 'z'],
    'q': ['t'],
    'r': ['u', 'y'],
    's': ['r'],
    't': [],
    'u': ['t', 'n'],
    'v': ['w', 'x', 'o'],
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
        return 'v:{}\tpi:{}\td-f:{}-{}\tc:{}'.format(self.val, parent, self.d, self.f, self.color)


def initialize_graph(graph):
    vertices = {v:Vertex(v) for v in graph}
    for vertex in vertices:
        vertices[vertex].update_edges(graph[vertex], vertices)
    return vertices


def simple_path(u, v, local_path):
    if u.val == v.val:
        #print('reached: {}'.format(local_path + v.val))
        return 1
    elif u.paths > 0:
        return u.paths
    else:
        if not u.edges:
            #print('empty: {} -> {}'.format(u.val, u.paths))
            pass
        for vertex in u.edges:
            #print('cur path {} and node {}, updated with {} and {}'.format(u.paths, u.val, vertex.val, v.val))
            u.paths = u.paths + simple_path(vertex, v, local_path + u.val)
        return u.paths

def compute_paths(graph):
    print('\ncheck the total avaialble path')
    vertices = initialize_graph(graph)
    for vertex in vertices:
        vertices[vertex].paths = 0
    mz_path = simple_path(vertices['p'], vertices['v'], '')
    print('total paths {}'.format(mz_path))


def shortest_path_print(source, target):
    if source.val == target.val:
        print(source.val)
    elif target.pi is None:
        print('no available path')
    else:
        shortest_path_print(source, target.pi)
        print(target.val)


def bfs(at, visited, sub_graph, graph):
    visited[at] = True
    neighbours = graph[at]
    for vertex in neighbours:
        if visited[vertex] == False:
            pass

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

def dfs_colored(graph):
    '''colored dfs approach from intro_algo'''
    vertices = initialize_graph(graph)
    time = 0
    has_circle = False

    def dfs_visit(vertex):
        nonlocal time
        nonlocal has_circle
        time = time + 1
        vertex.d = time
        vertex.color = 'g'
        for linked_vertex in vertex.edges:
            if linked_vertex.color == 'w':
                linked_vertex.pi = vertex
                dfs_visit(linked_vertex)
            else:
                source_vertex = vertex
                path = ''
                while source_vertex:
                    path += source_vertex.val
                    if source_vertex is linked_vertex:
                        has_circle = True
                        print('found circle {}'.format(path))
                        break
                    source_vertex = source_vertex.pi

        vertex.color = 'b'
        time = time + 1
        vertex.f = time

    for name, vertex in vertices.items():
        if vertex.color == 'w':
            dfs_visit(vertex)
    return vertices, has_circle

def dfs_colored_stack(graph):
    vertices = initialize_graph(graph)
    time = 0
    stack = []

    for v in vertices:
        if vertices[v].color == 'w':
            stack.append(vertices[v])
            #vertices[v].color = 'g'
        while stack:
            u = stack.pop()
            time = time + 1
            u.d = time
            for vertex in u.edges:
                if vertex.color == 'w':
                    vertex.pi = u
                    vertex.color = 'g'
                    stack.append(vertex)
            time += 1
            u.f = time
    return vertices


def dfs(at, visited, sub_graph, graph):
    visited[at] = True
    neighbours = graph[at]
    for next in neighbours:
        if visited[next] == False:
            dfs(next, visited, sub_graph, graph)
    sub_graph.append(at)

def circle_detect(graph):
    vertices = initialize_graph(graph)


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

# compute the number of paths from one node to another:
# compute_paths(g_22_8)

print('\ncolored stacked dfs: finished time not working')
vertices = dfs_colored_stack(g_22_8)
for key, vertex in vertices.items():
    print(vertex)



#dfs_colored(g)
print('\ncolored recursive dfs')
vertices, has_circle = dfs_colored(g_circle)
print('g_22_8 has circle: {}'.format(has_circle))
for name, vertex in vertices.items():
    print(name, vertex)


vertices = initialize_graph(g)
bfs_color(vertices, 0)
#for vertex in vertices:
#    print(vertex, vertices[vertex])
print('\nshortest path on vertices')
shortest_path_print(vertices[0], vertices[4])

print('\nsorted:', top_sort(g))

print('\nglobal nonlocal test')
var1 = 10
#print(id(var1))
def test_fun(ab):
    var1 = ab + 1
    #print(id(var1))
    def fun():
        global var1
        # nonlocal var1
        #print(id(var1))
        var1 = var1 + 20
        print('var1 is', var1)

    fun()
    print('var1 is', var1)

test_fun(2)
