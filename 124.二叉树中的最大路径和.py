#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-inf]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, root, res):
        if not root: return 0
        resLeft, resRight = [-inf], [-inf]
        left = max(0, self.dfs(root.left, resLeft))
        right = max(0, self.dfs(root.right, resRight))
        res[0] = max(resLeft[0], resRight[0])
        res[0] = max(res[0], root.val+left+right)
        return root.val + max(left, right)
# @lc code=end

