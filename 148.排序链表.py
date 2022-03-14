#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        h1, h2 = head, self.split(head)
        h1, h2 = self.sortList(h1), self.sortList(h2)
        return self.merge(h1, h2)
    def split(self, head):
        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node = slow.next
        slow.next = None
        return node
    def merge(self, h1, h2):
        root = cur = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                h1 = h1.next
            else:
                cur.next = h2
                h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        return root.next
# @lc code=end

