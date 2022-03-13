#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, path):
        if not node:
            return 0
        path = path*10 + node.val
        if not (node.left or node.right):
            return path
        return self.dfs(node.left, path) + self.dfs(node.right, path)

# @lc code=end

