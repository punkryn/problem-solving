# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.arr = []
        self.traversal(root, self.arr)
        self.ptr = 0

    def next(self) -> int:
        ret = self.arr[self.ptr]
        self.ptr += 1
        return ret

    def hasNext(self) -> bool:
        return self.ptr < len(self.arr)
    
    def traversal(self, x, arr):
        if x is None:
            return
        self.traversal(x.left, arr)
        arr.append(x.val)
        self.traversal(x.right, arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()