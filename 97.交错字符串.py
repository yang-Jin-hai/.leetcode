#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, t = len(s1), len(s2), len(s3)
        if m > n: return self.isInterleave(s2, s1, s3)
        if m + n != t: return False
        if m == 0: return s2 == s3
        dp = [[False] * (n+1) for i in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = s1[:i] == s3[:i]
        for i in range(1, n+1):
            dp[0][i] = s2[:i] == s3[:i]
        dp[0][0] = True
        for i in range(m):
            for j in range(n):
                if s1[i] == s3[i+j+1]:
                    dp[i+1][j+1] |= dp[i][j+1]
                if s2[j] == s3[i+j+1]:
                    dp[i+1][j+1] |= dp[i+1][j]
        return dp[-1][-1]
# @lc code=end

