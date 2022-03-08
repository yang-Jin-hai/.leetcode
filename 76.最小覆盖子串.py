#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from cmath import inf
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        hashtab = defaultdict(int)
        for i in range(n):
            hashtab[t[i]] += 1
        count = len(hashtab)
        l = r = min_l = min_r = 0
        min_length = inf
        while r < m or (count == 0 and r == m):
            if count > 0:
                if s[r] in hashtab:
                    hashtab[s[r]] -= 1
                    if hashtab[s[r]] == 0:
                        count -= 1
                r += 1
            else:
                if r - l < min_length:
                    min_length = r - l
                    min_l, min_r = l, r
                if s[l] in hashtab:
                    if hashtab[s[l]] == 0:
                        count += 1
                    hashtab[s[l]] += 1
                l += 1
        return s[min_l:min_r] if min_length < inf else ""

# @lc code=end

