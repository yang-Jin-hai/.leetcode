#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class posIterator:

    def __init__(self, root):
        self.stack = []
        self.cur = root

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        return val        

class negIterator:

    def __init__(self, root):
        self.stack = []
        self.cur = root

    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.right
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.left
        return val        
         
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        pos = posIterator(root)
        neg = negIterator(root)
        l, r = pos.next(), neg.next()
        while l < r:
            s = l + r
            if s < k: l = pos.next()
            elif s > k: r = neg.next()
            else: return True
        return False
        # (1)
        # record = defaultdict(int)
        # cur = root
        # stack = []
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     val = cur.val
        #     if k - val in record:
        #         return True
        #     record[val] = 1
        #     cur = cur.right
        # return False
# @lc code=end

