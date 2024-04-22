# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(preorder_left, preorder_right, postorder_left, postorder_right):
            root = TreeNode(preorder[preorder_left])
            if preorder_right == preorder_left:
                return root

            nxt = preorder_left + 1


            pos = postorder.index(preorder[nxt])
            cnt = pos - postorder_left

            root.left = construct(nxt, nxt + cnt, pos - cnt, pos)
            if nxt + cnt + 1 <= preorder_right:
                root.right = construct(nxt + cnt + 1, preorder_right, pos + 1, postorder_right - 1)

            return root
        
        n = len(preorder)
        return construct(0, n - 1, 0, n - 1)