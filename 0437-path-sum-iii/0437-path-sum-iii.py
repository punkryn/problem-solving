# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        def go(node, cur_sum):
            if node is None:
                return 0
            
            cur_sum += node.val
            ret = prefix.get(cur_sum - targetSum, 0)

            prefix[cur_sum] += 1
            ret += go(node.left, cur_sum) + go(node.right, cur_sum)
            prefix[cur_sum] -= 1
            return ret
        
        return go(root, 0)