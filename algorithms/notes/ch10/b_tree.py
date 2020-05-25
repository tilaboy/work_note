class BTreeNode:
    def __init__(self,
                 value: int,
                 p: 'BTreeNode'=None,
                 l: 'BTreeNode'=None,
                 r: 'BTreeNode'=None):
        self.p = p
        self.value = value
        self.l = l
        self.r = r

    def __str__(self):
        return 'v: {}, p: {}'.format(self.value, self.p)

    def children(self):
        leaf_nodes = []
        if self.l != None:
            leaf_nodes.append(self.l)
        if self.r != None:
            leaf_nodes.append(self.r)
        return leaf_nodes

class BTree:
    def __init__(self, arr):
        parent = None

        self.btree = self._build_tree(arr, len(arr), 0, parent)

    @classmethod
    def _build_tree(cls, arr, length, index, parent):
        # if no child return the node
        if (2 * (index + 1)) > length:
            return BTreeNode(arr[index], parent)
        elif (2 * (index + 1)) == length:
            l_node = cls._build_tree(arr, length, 2 * index + 1, None)
            r_node = None
            p_node = BTreeNode(arr[index], parent, l_node, r_node)
            l_node.p = p_node
            return p_node
        else:
            l_node = cls._build_tree(arr, length, 2 * index + 1, None)
            r_node = cls._build_tree(arr, length, 2 * index + 2, None)
            p_node = BTreeNode(arr[index], parent, l_node, r_node)
            l_node.p = p_node
            r_node.p = p_node
            return p_node

    def __str__(self):
        node = self.btree
        string = str(node) + '\n'

        BTree.walk_through(node)
        return string

    @staticmethod
    def walk_through(node):
        print(node)
        if node.l is not None:
            BTree.walk_through(node.l)
        if node.r is not None:
            BTree.walk_through(node.r)

    def run_through(self):
        node = self.btree
        children = node.children()
        print(node)
        while children:
            child = children.pop(0)
            print(child)
            children.extend(child.children())

    def tough_run_through(self):
        node = self.btree
        prev = None

        while(node is not None):
            if prev == node.p:
                print(node)
                prev = node
                if node.l is not None:
                    node = node.l
                elif node.r is not None:
                    node = node.r
                else:
                    node = node.p
            elif prev == node.l and node.r is not None:
                prev = node
                node = node.r
            else:
                prev = node
                node = node.p



    def drag_through(self, n):
        node = self.btree
        print(node)
        n -= 1
        while n > 0:
            print(node)
            # from left to right

    @staticmethod
    def search(node, key_value):
        if node.value == key_value:
            return node
        else:
            if node.l is not None:
                return search(node.l, key_value)
            if node.r is not None:
                return search(node.r, key_value)

sequence=[6,3,2,9,5,7,1,8,0,4]
btree = BTree(sequence)
btree.tough_run_through()
