#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
from functools import lru_cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        m = len(questions)
        dp = [questions[-1][0]] * m
        for i in range(m-2, -1, -1):
            score = questions[i][0]
            if i+questions[i][1]+1 < m:
                score += dp[i+questions[i][1]+1]
            dp[i] = max(score, dp[i+1])
        return dp[0]
        # @lru_cache(None)
        # def dp(i):
        #     if i > len(questions)-1:
        #         return 0
        #     return max(questions[i][0] + dp(i+questions[i][1]+1), dp(i+1))
        # return dp(0)
# @lc code=end

