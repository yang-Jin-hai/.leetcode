#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        start = max_length = 0
        for i, v in enumerate(s):
            if v in record and start <= record[v]:
                start = record[v] + 1
            else:
                max_length = max(max_length, i - start + 1)
            record[v] = i
        return max_length
# @lc code=end

