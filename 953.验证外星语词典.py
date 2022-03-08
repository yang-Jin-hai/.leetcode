#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        toOrder = [-1] * 26
        for i, n in enumerate(order):
            toOrder[ord(n)-ord('a')] = i
        for i in range(1, len(words)):
            if not self.isSorted(words[i], words[i-1], toOrder):
                return False
        return True
    
    def isSorted(self, cur, pre, toOrder):
        m, n = len(cur), len(pre)
        for i in range(min(m, n)):
            curOrder, preOrder = toOrder[ord(cur[i])-ord('a')], toOrder[ord(pre[i])-ord('a')]
            if curOrder > preOrder:
                return True
            if curOrder < preOrder:
                return False
        return m >= n

# @lc code=end

