#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        while s:
            res.append(s[:k])
            s = s[k:]
        res[-1] += (k-len(res[-1])) * fill
        return res
# @lc code=end

