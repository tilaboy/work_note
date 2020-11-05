class Vertex:
    def __init__(self, val):
        self.color = 'w'
        self.d = 0
        self.pi = None
        self.f = 0
        self.val = val
        self.edges = list()

    def reset(self):
        self.color = 'w'
        self.d = 0
        self.f = 0
        self.pi = None

    def update_edges(self, edges, vertices):
        self.edges = [vertices[e] for e in edges]

    def __str__(self):
        parent = self.pi.val if self.pi else None
        return 'v:{}\tpi:{}\td-f:{}-{}\tc:{}'.format(self.val, parent, self.d, self.f, self.color)


class Graph:
    def __init__(self, graph):
        vertices = {v:Vertex(v) for v in graph}
        self.nr_nodes = len(vertices)
        self.nr_edges = 0
        for vertex in vertices:
            self.nr_edges += len(graph[vertex])
            vertices[vertex].update_edges(graph[vertex], vertices)
        self.node_values = list(vertices.keys())
        self.nodes = vertices

    def reset_graph(self):
        for node_val in self.nodes:
            self.nodes[node_val].reset()

    def bfs(self):
        self.reset_graph()
        node_value = self.node_values[0]
        node = self.nodes[node_value]
        node.color = 'g'
        queue = [node]

        while queue:
            node = queue.pop(0)
            print('check child of node: {} in {}'.format(node.val, node.color))
            for child in node.edges:
                if child.color is 'w':
                    print('found {}'.format(child.val))
                    child.pi = node
                    child.color = 'g'
                    queue.append(child)
            print('make node {} to black'.format(node.val))
            node.color = 'b'
