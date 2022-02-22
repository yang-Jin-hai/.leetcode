#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0]:
            return 0 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @lru_cache
        def dfs(m, n):
            if m < 0 or n < 0 or obstacleGrid[m][n]:
                return 0
            if m == 0 and n == 0:
                return 1 - obstacleGrid[0][0]
            if m == 0:    
                return dfs(m, n-1)
            if n == 0:
                return dfs(m-1, n)
            return dfs(m-1, n) + dfs(m, n-1)
        return dfs(m-1, n-1)
# @lc code=end

