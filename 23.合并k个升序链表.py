#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return
        start, end = 0, len(lists)
        return self._mergeKLists(lists, start, end)
    def _mergeKLists(self, lists, start, end):
        if start + 1 == end:
            return lists[start]
        mid = (start + end) >> 1
        h1, h2 = self._mergeKLists(lists, start, mid), self._mergeKLists(lists, mid, end)
        h = self.merge(h1, h2)
        return h
    def merge(self, h1, h2):
        root = cur = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                cur.next = h1
                cur = cur.next
                h1 = h1.next
            else:
                cur.next = h2
                cur = cur.next
                h2 = h2.next
        if h1:
            cur.next = h1
        else:
            cur.next = h2
        return root.next
        # (1)
        # ListNode.__lt__ = lambda a, b: 0
        # heap = []
        # for l in lists:
        #     if l:
        #         heappush(heap, (l.val, l))
        # root = cur = ListNode()
        # while heap:
        #     cur.next = heappop(heap)[1]
        #     cur = cur.next
        #     if cur.next:
        #         heappush(heap, (cur.next.val, cur.next))
        # return root.next
# @lc code=end

