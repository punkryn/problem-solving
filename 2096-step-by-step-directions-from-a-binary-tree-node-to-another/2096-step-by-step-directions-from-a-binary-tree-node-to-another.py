# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath, destPath = self.LCA(root, startValue, destValue)
        if len(startPath) == 0:
            return ''.join(destPath)
        if len(destPath) == 0:
            return 'U' * len(startPath)
        
        return 'U' * len(startPath) + ''.join(destPath)

        
    def LCA(self, root, startValue, destValue):
        startPath = []
        destPath = []

        self.traversal(root, startValue, destValue, [], startPath, destPath)
        for i in range(min(len(startPath), len(destPath))):
            if startPath[i] != destPath[i]:
                return startPath[i:], destPath[i:]
        
        diff = min(len(startPath), len(destPath))
        return startPath[diff:], destPath[diff:]
        
    def traversal(self, node, startValue, destValue, path, startPath, destPath):
        if node == None:
            return
        
        if node.val == startValue:
            for p in path:
                startPath.append(p)
        
        if node.val == destValue:
            for p in path:
                destPath.append(p)
        
        path.append('L')
        self.traversal(node.left, startValue, destValue, path, startPath, destPath)
        path.pop()

        path.append('R')
        self.traversal(node.right, startValue, destValue, path, startPath, destPath)
        path.pop()