from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def split_in_order(left_inorder, right_inorder, left_preorder, right_preorder):
            nonlocal inorder
            nonlocal preorder
            if right_inorder < left_inorder:
                return None
            parent_node = preorder[left_preorder]
            id_parent_in_inorder = inorder.index(parent_node)
            nr_left = id_parent_in_inorder - left_inorder
            return TreeNode(
                parent_node,
                left=split_in_order(left_inorder, id_parent_in_inorder - 1, left_preorder + 1, left_preorder + nr_left),
                right=split_in_order(id_parent_in_inorder + 1, right_inorder, left_preorder + nr_left + 1, right_preorder)
            )
        return split_in_order(0, len(inorder) - 1, 0 , len(preorder) - 1)



sol = Solution()

tree_array = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
print(tree_array)
