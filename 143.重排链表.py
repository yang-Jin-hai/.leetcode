#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        root = ListNode(next=head)
        fast = slow = root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        flag, cur, pre = slow, slow.next, None
        while cur:
            next = cur.next
            cur.next = pre
            pre, cur = cur, next
        flag.next = None
        while head.next:
            next1, next2 = head.next, pre.next
            head.next = pre
            pre.next = next1
            pre = next2
            head = next1
        if pre:
            head.next = pre
# @lc code=end

