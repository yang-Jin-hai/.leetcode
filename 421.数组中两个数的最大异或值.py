#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = 2 * [None]
    def insert(self, num):
        node = self
        for i in reversed(range(32)):
            digit = (num >> i) & 1
            if node.children[digit] == None:
                node.children[digit] = Trie()
            node = node.children[digit]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        for num in nums:
            root.insert(num)
        res = 0
        for num in nums:
            node = root
            xor = 0
            for i in reversed(range(32)):
                digit = (num >> i) & 1
                if node.children[1-digit] != None:
                    xor = (xor << 1) + 1
                    node = node.children[1-digit]
                else:
                    xor = xor << 1
                    node = node.children[digit]
            res = max(xor, res)
        return res
# @lc code=end

