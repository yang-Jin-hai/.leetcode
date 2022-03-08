#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
        # (1)
        # m, n = 0, 0
        # p, q = headA, headB
        # while p:
        #     m += 1
        #     p = p.next
        # while q: 
        #     n += 1
        #     q = q.next
        # if m > n:
        #     return self.getIntersectionNode(headB, headA)
        # p, q = headA, headB
        # while m != n:
        #     n -= 1
        #     q = q.next
        # while p and p != q:
        #     p, q = p.next, q.next
        # return p if p else None
# @lc code=end

