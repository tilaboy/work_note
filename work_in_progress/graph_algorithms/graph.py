from __init__ import LOGGER

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.edge = None
        self.d = None
        self.f = None
        self.pi = None

    def reset(self):
        self.d = None
        self.f = None
        self.pi = None

    def nr_edges(self):
        edge = self.edge
        nr_edges = 0
        while edge is not None:
            nr_edges += 1
            edge = edge.next_edge
        return nr_edges

    def __str__(self):
        all_edge_vals = list()
        cur_edge = self.edge
        while cur_edge is not None:
            all_edge_vals.append(cur_edge.node.val)
            cur_edge = cur_edge.next_edge

        return "val: {}, edges: {}".format(self.val, all_edge_vals)


class GraphEdgeNode:
    def __init__(self, node: GraphNode):
        self.node = node
        self.next_edge = None


class Graph:
    '''
    Graph class, properties:
    - nodes: GraphNode object
    - nr_nodes: int
    - nr_edges: int
    '''
    def __init__(self, graph):
        self.nodes = list()
        self.nr_nodes = 0
        self.nr_edges = 0
        self.time = 0
        self.has_circle = False
        for node_val in graph:
            self.nodes.append(GraphNode(node_val))
            self.nr_nodes += 1
        for node_val, node_edges in graph.items():
            node = self.get_node(node_val, self.nodes)
            prev_linked_node = None
            for edge_val in node_edges:
                self.nr_edges += 1
                edge_node = GraphEdgeNode(self.get_node(edge_val, self.nodes))
                if node.edge is None:
                    node.edge = edge_node
                else:
                    prev_linked_node.next_edge = edge_node
                prev_linked_node = edge_node

    @staticmethod
    def get_node(val, nodes):
        for node in nodes:
            if node.val == val:
                return node
        else:
            return None

    def reset_graph(self):
        self.time = 0
        for node in self.nodes:
            node.reset()

    def __str__(self):
        rep = ''
        for node in self.nodes:
            rep += str(node) + '\n'
        return rep

    def bfs(self):
        self.reset_graph()
        visited = {node: 0 for node in self.nodes}
        for cur_node in self.nodes:
            if visited[cur_node]:
                continue
            queue = [cur_node]
            visited[cur_node] = 1
            cur_node.d = 0
            while queue:
                node = queue.pop(0)
                LOGGER.debug('check edge from node {}'.format(node.val))
                edge = node.edge
                while edge is not None:
                    if not visited[edge.node]:
                        LOGGER.debug('\tedge {}'.format(edge.node.val))
                        edge.node.pi = node
                        edge.node.d = node.d + 1
                        visited[edge.node] = 1
                        queue.append(edge.node)
                    edge = edge.next_edge

    def scc_detect(self):
        self.reset_graph()
        scc = dict()
        visited = {node: 0 for node in self.nodes}
        prev_visited = dict(visited)
        for cur_node in self.nodes:
            if visited[cur_node] == 0:
                LOGGER.debug('start a new tree: {}'.format(cur_node.val))
                self._dfs(cur_node, visited)
                tree_nodes = ''.join([node.val
                              for node in visited
                              if visited[node] > 0 and prev_visited[node] == 0])
                for node in visited:
                    if visited[node] > 1:
                        visited[node] = 1
                        if node.val in tree_nodes:
                            print('\t{} inside {}'.format(node.val, tree_nodes))
                        else:
                            for known_scc in scc:
                                if node.val in known_scc:
                                    print('\t{} from [{}], link to {}'.format(node.val, known_scc, tree_nodes))
                                    if tree_nodes not in scc[known_scc]:
                                        scc[known_scc].append(tree_nodes)
                                    break
                            else:
                                print('no scc found for {}, scc: {}'.format(node.val, scc))

                scc[tree_nodes] = list()
                prev_visited = dict(visited)
            else:
                LOGGER.debug('node {} already visisted'.format(cur_node.val))
        return scc


    def dfs(self):
        self.reset_graph()
        visited = {node: 0 for node in self.nodes}
        for cur_node in self.nodes:
            if not visited[cur_node]:
                LOGGER.debug('start a new tree: {}'.format(cur_node.val))
                self._dfs(cur_node, visited)
            else:
                LOGGER.debug('node {} already visisted'.format(cur_node.val))

    def _dfs(self, node, visited):
        LOGGER.debug('check node {} at {}'.format(node.val, self.time))
        self.time += 1
        node.d = self.time
        visited[node] = 1
        edge = node.edge
        while edge is not None:
            if visited[edge.node] == 0:
                edge.node.pi = node
                LOGGER.debug('check edge {} of node {}'.format(edge.node.val, node.val))
                self._dfs(edge.node, visited)
            else:
                # if child is ancestor of the node when node -> child and child is visited
                visited[edge.node] += 1
                circle = self._ancestors(node, edge.node)
                if circle:
                    print('circle: {}'.format(circle))
                    self.has_circle = True
                LOGGER.debug('{} visited (now from {})'.format(edge.node.val, node.val))
            edge = edge.next_edge
        self.time += 1
        node.f = self.time

    @staticmethod
    def _ancestors(node_child, node):
        ancestors = ''
        while node_child:
            ancestors += node_child.val
            if node_child.val == node.val:
                return ancestors
            node_child = node_child.pi
        else:
            return None

    def top_sort(self):
        # O(V + E) + O(V * logV): dfs + sorting
        # a faster way: add to the head of linked-list when node.f updated
        self.dfs()
        return [node for node in sorted(self.nodes, key=lambda x:x.f, reverse=True)]

    def top_sort_zero_degree(self):
        node_nr_edges = {node: 0 for node in self.nodes}
        for node in self.nodes:
            edge = node.edge
            while edge is not None:
                node_nr_edges[edge.node] += 1
                edge = edge.next_edge
        queue = [node for node in node_nr_edges if node_nr_edges[node] == 0]
        sorted_nodes = list()
        while queue:
            node = queue.pop(0)
            sorted_nodes.append(node)
            edge = node.edge
            while edge is not None:
                node_nr_edges[edge.node] -= 1
                if node_nr_edges[edge.node] == 0:
                    queue.append(edge.node)
                if node_nr_edges[edge.node] < 0:
                    LOGGER.info('decrease cause {}: from {} to {}'.format(
                        node_nr_edges[edge.node], node.val, edge.node.val
                    ))
                edge = edge.next_edge
        return sorted_nodes

    def find_all_path(self, val_u, val_v):
        def _path_find(node_u, node_v, local_path, all_paths):
            if node_u.val == node_v.val:
                all_paths.append(local_path)
                return 1
            else:
                if node_u.f <= node_v.f:
                    return 0
                else:
                    edge = node_u.edge
                    while edge is not None:
                        _path_find(edge.node, node_v, local_path + edge.node.val, all_paths)
                        edge = edge.next_edge

        node_u = self.get_node(val_u, self.nodes)
        node_v = self.get_node(val_v, self.nodes)

        # need node_u.f >= node_v.f
        if node_u.f < node_v.f:
            node_u, node_v = node_v, node_u
        paths = list()
        _path_find(node_u, node_v, node_u.val, paths)
        return paths

    def shortest_path_find(self, val_u, val_v):
        def _path_find(node_u, node_v, local_path):
            if node_u.val == node_v.val:
                print(local_path[::-1])
                return 1
            else:
                if node_u.d >= node_v.d:
                    return 0
                else:
                    node_v = node_v.pi
                    return _path_find(node_u, node_v, local_path + node_v.val)

        node_u = self.get_node(val_u, self.nodes)
        node_v = self.get_node(val_v, self.nodes)
        if node_u.d > node_v.d:
            node_v, node_u = node_u, node_v
        _path_find(node_u, node_v, node_v.val)

    def _transpose(self):
        trans_graph = {node.val: []
                       for node in
                       sorted(self.nodes, key=lambda node:node.f, reverse=True)
                       }
        for node in self.nodes:
            edge = node.edge
            while edge is not None:
                if edge.node.val in trans_graph:
                    trans_graph[edge.node.val].append(node)
                else:
                    trans_graph[edge.node.val] = [node]
                edge = edge.next_edge
        for node in self.nodes:
            if node.val in trans_graph:
                edges = trans_graph[node.val]
                trans_graph[node.val] = [
                    node.val
                    for node in
                    sorted(edges, key=lambda node:node.f, reverse=True)]
            else:
                trans_graph[node.val] = []

        return trans_graph
