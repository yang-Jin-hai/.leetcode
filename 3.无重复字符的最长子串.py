#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        ans = l = 0
        hashtab = {}
        for i, x in enumerate(s):
            if x in hashtab and l <= hashtab[x]:
                l = hashtab[x] + 1
            else:
                ans = max(ans, i-l+1)
            hashtab[x] = i
        return ans

# @lc code=end

