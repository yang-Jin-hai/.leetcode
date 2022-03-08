#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res, m = 0, len(s)
        def findSubstrings(l, r):
            count = 0
            while l >= 0 and r < m and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
            return count
        for i in range(m):
            res += findSubstrings(i, i)
            res += findSubstrings(i, i+1)
        return res
# @lc code=end

