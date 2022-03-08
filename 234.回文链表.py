#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        pre, cur = None, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre, cur = cur, next
        while pre:
            if pre.val != head.val:
                return False
            pre, head = pre.next, head.next
        return True
        # (1)
        # data = []
        # while head:
        #     data.append(head.val)
        #     head = head.next
        # l, r = 0, len(data)-1
        # while l < r:
        #     if data[l] != data[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True 
# @lc code=end

