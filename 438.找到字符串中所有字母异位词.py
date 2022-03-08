#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        res = []
        if m < n:
            return []
        record = [0] * 26
        for i in range(n):
            record[ord(p[i])-ord('a')] += 1
            record[ord(s[i])-ord('a')] -= 1
        if not any(record):
            res.append(0)
        for i in range(n, m):
            record[ord(s[i])-ord('a')] -= 1
            record[ord(s[i-n])-ord('a')] += 1
            if not any(record):
                res.append(i-n+1)
        return res
# @lc code=end

