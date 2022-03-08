#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new

        # (1)
        # if not head:
        #     return head
        # pre, cur = None, head
        # while cur:
        #     next = cur.next
        #     cur.next = pre
        #     pre, cur = cur, next
        # return pre
# @lc code=end

