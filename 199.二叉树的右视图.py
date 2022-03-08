#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue1 = deque([root])
        queue2 = deque()
        res = [root.val]
        while queue1:
            node = queue1.popleft()
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                queue1, queue2 = queue2, queue1
                if queue1:
                    res.append(queue1[-1].val)
        return res
# @lc code=end

