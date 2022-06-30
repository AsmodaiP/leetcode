# Definition for a binary tree node.



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        stack = [(root, -sys.maxsize-1, sys.maxsize)]
        while stack:
            node, maximum, minimum = stack.pop()
            if not node:
                continue
            if node.val <= maximum or node.val >= minimum:
                return False
            
            stack.append((node.left, maximum, node.val))
            stack.append((node.right, node.val, minimum))
        return True
