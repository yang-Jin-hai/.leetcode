#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class ListNode:

    def __init__(self, key=0, val=0, pre=None, nxt=None):
        self.key, self.val, self.pre, self.nxt = key, val, pre, nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = ListNode(), ListNode()
        self.head.nxt, self.tail.pre = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            self.moveToTail(node, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.moveToTail(self.cache[key], value)
        else:
            if len(self.cache) == self.capacity:
                leastUsedNode = self.head.nxt
                self.delete(leastUsedNode)
                self.cache.pop(leastUsedNode.key)
            node = ListNode(key=key, val=value)
            self.insertToTail(node)
            self.cache[key] = node

    def moveToTail(self, node, new_val):
        self.delete(node)
        node.val = new_val
        self.insertToTail(node)

    def delete(self, node):
        node.pre.nxt, node.nxt.pre = node.nxt, node.pre

    def insertToTail(self, node):
        node.pre, node.nxt = self.tail.pre, self.tail
        self.tail.pre.nxt, self.tail.pre = node, node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

