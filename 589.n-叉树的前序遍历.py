#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack.extend(node.children[::-1])
        return res
        # res = []
        # def dfs(root):
        #     if not root: return 
        #     res.append(root.val)
        #     for child in root.children:
        #         dfs(child)
        # dfs(root)
        # return res
# @lc code=end

