import sys
from typing import List
import time
from examples import get_cases

class Node:
    def __init__(self, val, children=list()):
        self.val = val
        self.children = children

    def find_child(self, val):
        if not self.children:
            return None
        if self.children[0].val == val:
            return self.children[0]
        for child in self.children[1:]:
            if child.val == val:
                return child
        return None

def print_tree(node):
    str_tree = list()
    stack = [node]
    while stack:
        nr_nodes = len(stack)
        for i_node in range(nr_nodes):
            stack.extend(stack[i_node].children)
        str_tree.append([node.val for node in stack[:nr_nodes]])
        stack = stack[nr_nodes:]
    print(" => ".join([str(layer) for layer in str_tree]))

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def add_path_to_tree(node, sub_arr):
            len_arr = len(sub_arr)
            i = 0
            while i < len_arr:
                city = sub_arr[i]
                child = node.find_child(city)
                if child is None:
                    child = Node(city, list())
                    node.children.append(child)
                node = child
                i += 1

        def construct_tree(path_arr):
            root = Node(-1, list())
            for i in range(len(path_arr)):
                add_path_to_tree(root, path_arr[i:])
            return root

        def filter_at_pos(node, path_arr, i, len_path, new_node):
            while i < len_path:
                city = path_arr[i]
                child = node.find_child(city)
                if child is None:
                    break
                else:
                    new_child = new_node.find_child(city)
                    if new_child is None:
                        new_child = Node(city, list())
                        new_node.children.append(new_child)
                    new_node = new_child
                    node = child
                i += 1

        def filter_tree(tree, path_arr):
            len_path = len(path_arr)
            i_city = 0
            new_tree = Node(-1, list())
            while i_city < len_path:
                filter_at_pos(tree, path_arr, i_city, len_path, new_tree)
                i_city += 1
            return new_tree

        def get_tree_longest_path(node, path_len):
            nonlocal tree_longest_path
            for child in node.children:
                #print("child:", child.val)
                if path_len + 1 > tree_longest_path:
                    tree_longest_path = path_len + 1
                get_tree_longest_path(child, path_len + 1)

        _, i_shortest = min((len(path), i_path) for (i_path, path) in enumerate(paths))
        root = construct_tree(paths[i_shortest])
        for i in range(len(paths)):
            if i == i_shortest:
                continue
            else:
                root = filter_tree(root, paths[i])
        tree_longest_path = 0
        get_tree_longest_path(root, 0)
        return tree_longest_path


cases = get_cases()
K = 6
sol = Solution()
start = time.perf_counter_ns()
for case in cases[:K]:
    result = sol.longestCommonSubpath(case["n"], case["input"])
    #print(case["n"], case["input"], result)
    assert result == case['expect']
print("durantion: {}".format((time.perf_counter_ns() - start)/1e9))
