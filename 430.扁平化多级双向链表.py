#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.flattenGetTail(head)
        return head

    def flattenGetTail(self, head):
        tail = None
        node = head
        while node:
            next = node.next
            if node.child:
                child = node.child
                tail = childTail = self.flattenGetTail(child)
                node.child = None
                childTail.next = next
                node.next = child
                child.prev = node
                if next:
                    next.prev = childTail
            else:
                tail = node
            node = next
        return tail
# @lc code=end

