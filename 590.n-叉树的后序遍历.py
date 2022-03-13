#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res, stack, prev = [], [root], None
        while stack:
            cur = stack[-1]
            if cur.children and cur.children[-1] != prev:
                stack.extend(cur.children[::-1])
            else:
                cur = stack.pop()
                prev = cur
                res.append(cur.val)
        return res
        # (1)
        # res = []
        # def dfs(root):
        #     if not root: return
        #     for child in root.children:
        #         dfs(child)
        #     res.append(root.val)
        #     return
        # dfs(root)
        # return res
# @lc code=end

