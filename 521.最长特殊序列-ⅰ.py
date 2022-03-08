#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) < len(b):
            a, b = b, a
        return len(a) if a != b else -1
# @lc code=end

