#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        record = [0] * len(words)
        for i, w in enumerate(words):
            for c in w:
                record[i] |= 1 << (ord(c)-ord('a'))
            for j in range(i):
                if not record[i] & record[j]:
                    res = max(res, len(words[i] * len(words[j])))
        return res
# @lc code=end

