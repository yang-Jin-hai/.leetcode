#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from cmath import inf
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        queue1 = deque([root])
        queue2 = deque()
        cur_max = -inf
        while queue1:
            node = queue1.popleft()
            cur_max = max(cur_max, node.val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                queue1, queue2 = queue2, queue1
                res.append(cur_max)
                cur_max = -inf
        return res

# @lc code=end

