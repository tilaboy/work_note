# indorder print
class TreeNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.p = parent
        self.l = left
        self.r = right
        self.value = value

    def __str__(self):
        p = None if self.p is None else self.p.value
        l = None if self.l is None else self.l.value
        r = None if self.r is None else self.r.value
        return "{} (p:{}, l:{}, r:{})".format(self.value, p, l, r)


class BTree:
    def __init__(self):
        self.root = None

    def minimum(self, node):
        while node is not None:
            min_node = node
            node = node.l
        return min_node

    def maximum(self, node):
        while node is not None:
            max_node = node
            node = node.r
        return max_node

    def minimum_recur(self, node):
        if node is not None and node.l is not None:
            return self.minimum_recur(node.l)
        else:
            return node

    def maximum_recur(self, node):
        if node is not None and node.r is not None:
            return self.maximum_recur(node.r)
        else:
            return node



    def search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                break
            elif value > node.value:
                node = node.r
            else:
                node = node.l
        return node

    def successor(self, node):
        if node.r is not None:
            return self.minimum(node.r)
        else:
            node_p = node.p
            while node is not None and node_p is not None and node_p.r == node:
                node = node_p
                node_p = node.p
            return node_p

    def predecessor(self, node):
        if node.l is not None:
            return self.maximum(node.l)
        else:
            node_p = node.p
            while node is not None and node_p is not None and node_p.l == node:
                node = node_p
                node_p = node.p
            return node_p

    def insert(self, value):
        # start from the top
        # until none
        node = self.root
        node_p = None
        while node is not None:
            node_p = node
            if value > node.value:
                node = node.r
            else:
                node = node.l

        node = TreeNode(value, node_p, None, None)
        if self.root is None:
            self.root = node
        else:
            if node.value > node_p.value:
                node_p.r = node
            else:
                node_p.l = node

    def _which_child(self, node):
        child_type = ''
        if node.p is None:
            child_type = 'root'
        else:
            if node.p.l is not None and node.p.l.value == node.value:
                child_type = 'left'
            else:
                child_type = 'right'
        return child_type

    def _transport(self, node_x, node_y):
        '''transport the node_y to node_x'''
        child_type = self._which_child(node_x)
        if child_type == 'root':
            self.root = node_y
        elif child_type == 'left':
            node_x.p.l = node_y
        else:
            node_x.p.r = node_y
        if node_y is not None:
            node_y.p = node_x.p


    def delete(self, node):
        if node.l == None and node.r == None:
            self._transport(node, None)
        elif node.l == None:
            self._transport(node, node.r)
        elif node.r == None:
            self._transport(node, node.l)
        else:
            # has both left and right, the successor and predecessor must
            # be one of treenodes belowing current node
            successor = self.successor(node)
            print("using successor: {}".format(successor))
            if successor.r is None:
                raise ValueError('successor has no right child')
            if successor.l is not None:
                raise ValueError('successor has left child')

            if successor.p.value != node.value:
                print('to transplant successor: {} to {}'.format(successor.r, successor))
                self._transport(successor, successor.r)
                # replace node with successor
                print('to replace node with successor: {} to {}'.format(successor, node))
                self._transport(node, successor)
                successor.l = node.l
                successor.r = node.r
                node.l.p = successor
                node.r.p = successor
            else:
                print('to transplant successor: {} to {}'.format(successor, node))
                self._transport(node, successor)
                if node.l.value == successor.value:
                    successor.r = node.r
                    node.r.p = successor
                else:
                    successor.l = node.l
                    node.l.p = successor


    def _build(self, arr):
        for ele in arr:
            self.insert(ele)
            #self._print()

    def _print_inorder(self):
        def inorder(node):
            if node is not None:
                inorder(node.l)
                print(node.value, end=' ')
                inorder(node.r)
        inorder(self.root)
        print()

    def _print_postorder(self):
        def postorder(node):
            if node is not None:
                postorder(node.l)
                postorder(node.r)
                print(node.value, end=' ')
        postorder(self.root)
        print()


    def _print_inorder_iter(self):
        current = self.root
        stack = list()

        while stack or current is not None:
            if current is not None:
                stack.append(current)
                current = current.l
            elif stack:
                current = stack.pop()
                print(current.value, end= ' ')
                current = current.r
        print()

    def _print_preorder_iter(self):
        current = self.root
        stack = list()

        while stack or current is not None:
            if current is not None:
                stack.append(current)
                print(current.value, end= ' ')
                current = current.l
            elif stack:
                current = stack.pop()
                #print(current.value, end= ' ')
                current = current.r
        print()


    def _print_preorder(self, arr):
        def preorder(node):
            if node is not None:
                #print(node.value, end= ' ')
                arr.append(node.value)
                preorder(node.l)
                preorder(node.r)
        preorder(self.root)
        print()

    def _print_postorder(self):
        def postorder(node):
            if node is not None:
                postorder(node.l)
                postorder(node.r)
                print(node.value, end = ' ')
        postorder(self.root)
        print()

    def _total_nr_inorder(self):
        def inorder(node, nr):
            if node is not None:
                nr = inorder(node.l, nr)
                nr += 1
                nr = inorder(node.r, nr)
            return nr
        nr = inorder(self.root, 0)
        print("total", nr)



#arr = [15, 6, 18, 3, 9, 17, 20, 2, 4, 7, 13, 19, 8, 10, 14, 11, 12]
arr = [20, 10, 30, 5, 15, 25, 40, 13, 17]
test_tree = BTree()
test_tree._build(arr)
test_tree._print_inorder()
test_tree._print_postorder()
#test_tree._print_inorder_iter()
#test_tree._print_preorder()
#test_tree._print_preorder_iter()

preorder_list = list()
test_tree._print_preorder(preorder_list)
print(preorder_list)
test_tree._total_nr_inorder()
test_tree._print_postorder()
print("min: {}".format(test_tree.minimum_recur(test_tree.root)))
print("max: {}".format(test_tree.maximum_recur(test_tree.root)))

#print(arr)
#for ele in arr:
#    selected_node = test_tree.search(ele)
#    print('select {}'.format(selected_node))
#    print("successor: {}".format(test_tree.successor(selected_node)))
#    print("predecessor: {}".format(test_tree.predecessor(selected_node)))

#selected_node = test_tree.search(9)
#test_tree.delete(selected_node)
#test_tree._print()
