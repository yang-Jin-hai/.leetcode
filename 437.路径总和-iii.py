#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.record = defaultdict(int)
        self.record[0] = 1
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, path, targetSum):
        if not root: return 0
        path += root.val
        count = self.record[path-targetSum]
        self.record[path] += 1
        count += self.dfs(root.left, path, targetSum)
        count += self.dfs(root.right, path, targetSum)
        self.record[path] -= 1
        return count
# @lc code=end

