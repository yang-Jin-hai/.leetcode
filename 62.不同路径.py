#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1 for i in range(n)] for i in range(2)]
        dp = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]
        # return factorial(m+n-2) // factorial(n-1) // factorial(m-1)
# @lc code=end

