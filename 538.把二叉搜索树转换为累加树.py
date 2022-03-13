#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        presum = [0]
        def dfs(root):
            if not root: return
            dfs(root.right)
            presum[0] += root.val
            root.val = presum[0]
            dfs(root.left)
        dfs(root)
        return root
# @lc code=end

