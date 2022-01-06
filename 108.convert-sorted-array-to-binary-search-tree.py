#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0: return None
        pos = len(nums) >> 1
        root = TreeNode(val=nums[pos])
        root.left = self.sortedArrayToBST(nums[:pos])
        root.right = self.sortedArrayToBST(nums[pos+1:])
        return root

        # def traverse(begin, end):
        #     if end < begin: return None
        #     pos = (begin + end) >> 1
        #     root = TreeNode(val=nums[pos])
        #     root.left = traverse(begin, pos-1)
        #     root.right = traverse(pos+1, end)
        #     return root
        # return traverse(0, len(nums)-1)
# @lc code=end

