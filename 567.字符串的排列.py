#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        record = [0] * 26
        m, n = len(s1), len(s2)
        if m > n:
            return False
        for i in range(m):
            record[ord(s1[i])-ord('a')] += 1
            record[ord(s2[i])-ord('a')] -= 1
        if not any(record):
            return True
        for i in range(m, n):
            record[ord(s2[i])-ord('a')] -= 1
            record[ord(s2[i-m])-ord('a')] += 1
            if not any(record):
                return True
        return False
# @lc code=end

