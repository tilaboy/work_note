from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def create_tree(binary_strs):
            root = TreeNode('S')
            node = root
            for str in binary_strs:
                node = root
                for num in str:
                    if num == '0':
                        if node.left == None:
                            node.left = TreeNode('0')
                        node = node.left
                    if num == '1':
                        if node.right == None:
                            node.right = TreeNode('0')
                        node = node.right
            return root

        def find_first_single_leaf(node, arr):
            if node.left and node.right:
                left_leavs = find_first_single_leaf(node.left, arr + [node.left.val])
                if left_leavs:
                    return left_leavs
                right_leavs = find_first_single_leaf(node.right, arr + [node.right.val])
                if right_leavs:
                    return right_leavs
            elif node.left:
                return arr + ['1']
            elif node.right:
                return arr + ['0']
            else:
                return None

        root = create_tree(nums)
        n = len(nums[0])
        num_chars = find_first_single_leaf(root, list())
        position = len(num_chars)
        return ''.join(num_chars + ['0'] * (n - position))

sol = Solution()
cases = [
    {
        "input": ["01","10"],
        "expect": '00'
    },
    {
        "input": ["00","01"],
        "expect": '10'
    },
    {
        "input": ["111","011","001"],
        "expect": '000'
    },
]

for case in cases:
    result = sol.findDifferentBinaryString(case["input"])
    print(case["input"], result)
    assert result == case['expect']
