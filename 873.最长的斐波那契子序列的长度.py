#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        m = len(arr)
        record = {}
        for i, v in enumerate(arr):
            record[v] = i 
        dp = [[2 for i in range(m)] for i in range(m)] 
        res = 2
        for i in range(1, m):
            for j in range(i):
                k = record[arr[i]-arr[j]] if arr[i]-arr[j] in record else -1
                dp[j][i] = dp[k][j] + 1 if k >= 0 and k < j else 2
                res = max(res, dp[j][i])
                # print(dp, arr[i])
        return res if res > 2 else 0
# @lc code=end

