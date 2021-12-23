#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 and list2): return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        # if not (list1 and list2): return list1 or list2
        # end = res = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         end.next = ListNode(list1.val)
        #         end = end.next
        #         list1 = list1.next
        #     else:
        #         end.next = ListNode(list2.val)
        #         end = end.next
        #         list2 = list2.next
        # end.next = list1 or list2
        # return res.next

# @lc code=end

