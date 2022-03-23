#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m > n: return self.longestCommonSubsequence(text2, text1)
        dp = [[0 for i in range(n+1)] for i in range(2)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j] + 1
                else:
                    dp[(i+1)%2][j+1] = max(dp[i%2][j+1], dp[(i+1)%2][j])
        return dp[m%2][-1]
# @lc code=end

