#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
        return self.dfs(m-1, n-1)
    @lru_cache(None)
    def dfs(self, m, n):
        if m < 0 or n < 0:
            return 0
        if m == 0 or n == 0:
            return 1
        return self.dfs(m-1, n) + self.dfs(m, n-1)
# @lc code=end

