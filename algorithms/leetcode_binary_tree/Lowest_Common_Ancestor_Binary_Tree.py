class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def print_path(node_path):
            path_val = [node.val for node in node_path]
            print(' => '.join(path_val))


        def _search(node, target, parents):
            if node is None:
                return None
            elif node == target:
                return parents + [node]
            else:
                left_path = _search(node.left, target, parents + [node])
                right_path = _search(node.right, target, parents + [node])
                return left_path if left_path is not None else right_path

        p_path = _search(root, p, list())
        q_path = _search(root, q, list())

        print_path(p_path)
        print_path(q_path)

        share_node = root
        for p_path_node, q_path_node in zip(p_path, q_path):
            if p_path_node == q_path_node:
                share_node = p_path_node
            else:
                return share_node


sol = Solution()
sol.lowestCommonAncestor()
