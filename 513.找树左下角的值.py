#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue1 = deque([root])
        queue2 = deque()
        left = root
        while queue1:
            node = queue1.popleft()
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                queue1, queue2 = queue2, queue1
                if queue1:
                    left = queue1[0]
        return left.val

# @lc code=end

