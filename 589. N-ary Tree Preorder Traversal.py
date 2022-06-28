
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []

        def dfs(node: Node):
            if not node.val:
                return
            stack.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return stack
