# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.l = list()
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.traverse(root, self.l)
        
        return self.l
    
    def traverse(self, root: TreeNode, l: List[int]):
        if root:
            self.l.append(root.val)
            self.traverse(root.left, self.l)
            self.traverse(root.right, self.l)
        else:
            return None