# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        n = len(queries)

        ans = []

        arr = []
        def inorder(cur):
            nonlocal ans

            if cur is None:
                return
            
            inorder(cur.left)
            arr.append(cur.val)
            inorder(cur.right)
        
        inorder(root)

        for i in range(n):
            query = queries[i]

            idx = bisect.bisect_left(arr, query)
            if idx < len(arr) and query == arr[idx]:
                ans.append([query, query])
                continue
            
            tmp = [-1, -1]
            l = bisect.bisect_left(arr, query)
            if query > arr[0]:
                tmp[0] = arr[l - 1]
            
            r = bisect.bisect_left(arr, query)
            if r < len(arr):
                tmp[1] = arr[r]
            ans.append(tmp)

        return ans