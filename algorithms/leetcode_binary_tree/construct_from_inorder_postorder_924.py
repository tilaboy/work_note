from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def split_in_order(left_inorder, right_inorder, left_postorder, right_postorder):
            nonlocal inorder
            nonlocal postorder
            if right_inorder < left_inorder:
                return None
            parent_node = postorder[right_postorder]
            id_parent_in_inorder = inorder.index(parent_node)
            nr_left = id_parent_in_inorder - left_inorder
            return TreeNode(
                parent_node,
                left=split_in_order(left_inorder, id_parent_in_inorder - 1, left_postorder, left_postorder + nr_left - 1),
                right=split_in_order(id_parent_in_inorder + 1, right_inorder, left_postorder + nr_left, right_postorder - 1)
            )
        return split_in_order(0, len(inorder) - 1, 0 , len(postorder) - 1)



sol = Solution()

tree_array = sol.buildTree([9,3,15,20,7], [9,15,7,20,3])
print(tree_array)
