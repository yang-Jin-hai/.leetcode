#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return None
        slow = head.next
        fast = slow.next
        while fast != slow and fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if not fast:
            return None
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p
# @lc code=end

