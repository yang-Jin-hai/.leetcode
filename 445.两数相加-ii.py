#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1, q2 = deque(), deque()
        while l1:
            q1.append(l1.val)
            l1 = l1.next
        while l2:
            q2.append(l2.val)
            l2 = l2.next
        carry, res = 0, None
        while q1 or q2 or carry:
            v1 = v2 = 0
            if q1: v1 = q1.pop()
            if q2: v2 = q2.pop()
            s = v1 + v2 + carry
            carry, v = divmod(s, 10)
            res = ListNode(v, res)
        return res
        
        # if not l1: return l2
        # if not l2: return l1
        # pre, cur = None, l1
        # while cur:
        #     next = cur.next
        #     cur.next, pre, cur = pre, cur, next
        # l1 = pre
        # pre, cur = None, l2
        # while cur:
        #     next = cur.next
        #     cur.next, pre, cur = pre, cur, next
        # l2 = pre
        # carry = 0
        # res = None
        # while l1 or l2 or carry:
        #     v1 = v2 = 0
        #     if l1: 
        #         v1 = l1.val
        #         l1 = l1.next
        #     if l2: 
        #         v2 = l2.val
        #         l2 = l2.next
        #     s = v1 + v2 + carry
        #     carry, v = divmod(s, 10)
        #     res = ListNode(v, next=res)
        # return res

# @lc code=end

