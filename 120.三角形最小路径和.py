#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [0] * m
        dp[0] = triangle[0][0]
        for i in range(1, m):
            dp[i] = dp[i-1] + triangle[i][i]
            for j in range(1, i)[::-1]:
                dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)
# @lc code=end

