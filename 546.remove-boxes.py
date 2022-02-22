#
# @lc app=leetcode id=546 lang=python3
#
# [546] Remove Boxes
#

# @lc code=start
from functools import lru_cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(l, r, k):
            if l > r:
                return 0
            while l< r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            score = dfs(l, r-1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    score = max(score, dfs(l, i, k+1) + dfs(i+1, r-1, 0))
            return score
        return dfs(0, len(boxes)-1, 0)
# @lc code=end

