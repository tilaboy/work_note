from typing import List
from unittest import TestCase

class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left =  left
        self.right = right
        self.parent = parent
        self.size = self.get_size()

    def get_size(self):
        node_size = 1
        if self.left is not None:
            node_size += self.left.size
        if self.right is not None:
            node_size += self.right.size
        return node_size

    def __str__(self):
        return "{} left: {}, right: {}, parent:{}, size {}".format(
            self.val,
            None if self.left is None else self.left.val,
            None if self.right is None else self.right.val,
            None if self.parent is None else self.parent.val,
            self.size
        )

class OrderStatisticTree:
    def __init__(self, arr: List[int]):
        self.root = self._create_from_arr(arr)

    def _create_from_arr(self, arr):
        root = TreeNode(arr.pop(0))
        stack = [root]
        next_level_nodes = []
        node = None
        status = 'fetch'
        while arr or stack:
            if not stack:
                stack = next_level_nodes[:]
                next_level_nodes = []
            if node is not None:
                if status == 'left':
                    child = arr.pop(0) if arr else None
                    if child is None:
                        node.left = child
                    else:
                        node.left = TreeNode(child)
                        node.left.parent = node
                    status = 'right'
                    next_level_nodes.append(node.left)
                elif status == 'right':
                    child = arr.pop(0) if arr else None
                    if child is None:
                        node.right = child
                    else:
                        node.right = TreeNode(child)
                        node.right.parent = node
                    status = 'fetch'
                    next_level_nodes.append(node.right)
            else:
                status = 'fetch'
            while stack and status == 'fetch':
                node = stack.pop(0)
                status = 'left'
        return root

    def update_size(self):
        def _update(node):
            if node is None:
                return 0
            else:
                updated_right = _update(node.right)
                updated_left = _update(node.left)
                node.size = updated_left + updated_right + 1
                return node.size
        _update(self.root)

    def select_ith(self, i):
        def select_rec(node, i):
            print("node: {}\tleft:{}\ti: {}".format(node, node.left, i))
            if node.left is None:
                cur_size = 1
            else:
                cur_size = node.left.size + 1
            if i == cur_size:
                return node
            elif i < cur_size:
                return select_rec(node.left, i)
            else:
                return select_rec(node.right, i - cur_size)
        return select_rec(self.root, i)

    def __str__(self):
        node = self.root
        stack = [(node, 0)]
        result = ''
        current_level = 0
        while node or stack:
            node, level = stack.pop(0)
            if level > current_level:
                current_level = level
                result += '\n'
            if node is None:
                result += ' nil'
            else:
                result += " " + str(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return result

class TestTreeNode(TestCase):
    def test_single_tree_node(self):
        root = TreeNode(4)
        self.assertEqual(str(root), "4 left: None, right: None, parent:None, size 1")

    def test_single_tree_node(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.parent = root
        root.right.parent = root
        self.assertEqual(str(root), "4 left: 2, right: 7, parent:None, size 1")
        self.assertEqual(str(root.left), "2 left: None, right: None, parent:4, size 1")
        self.assertEqual(str(root.right), "7 left: None, right: None, parent:4, size 1")
        root.size = root.get_size()
        self.assertEqual(str(root), "4 left: 2, right: 7, parent:None, size 3")


class TestSimpleTree(TestCase):
    def setUp(self):
        self.tree = OrderStatisticTree([4, 2, 7])

    def test_const_simple_tree(self):
        self.assertEqual(str(self.tree), ' 4\n 2 7\n nil nil nil nil')

    def test_select_simple_tree(self):
        self.assertEqual(self.tree.select_ith(1).val, 2)
        self.assertEqual(self.tree.select_ith(2).val, 4)
        self.assertEqual(self.tree.select_ith(3).val, 7)


class TestMultiLevelTree(TestCase):
    def setUp(self):
        tree = OrderStatisticTree([26, 17, 41, 14, 21, 30, 47, 10, 16, 19, 21,
                                   28, 38, None, None, 7, 12, 14, None, None,
                                   20, None, None, None, None, 35, 39, 3])
        self.tree = tree

    def test_multilevel_tree(self):
        print(self.tree.root)
        print(self.tree.root.left)
        print(self.tree.root.right)
        tree_string = ''' 26
 17 41
 14 21 30 47
 10 16 19 21 28 38 nil nil
 7 12 14 nil nil 20 nil nil nil nil 35 39
 3 nil nil nil nil nil nil nil nil nil nil nil
 nil nil'''

        self.assertEqual(str(self.tree), tree_string)

    def test_tree_size_update(self):
        self.tree.update_size()
        self.assertEqual(self.tree.root.size, 20)
        self.assertEqual(self.tree.root.left.size, 12)

    def test_select_ith(self):
        self.tree.update_size()
        self.assertEqual(self.tree.select_ith(1).val, 3)
        self.assertEqual(self.tree.select_ith(2).val, 7)
        self.assertEqual(self.tree.select_ith(4).val, 12)
        self.assertEqual(self.tree.select_ith(13).val, 26)
        self.assertEqual(self.tree.select_ith(17).val, 38)
        self.assertEqual(self.tree.select_ith(19).val, 41)
