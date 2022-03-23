#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre = cur = 0
        for i in range(2, len(cost)+1):
            pre, cur = cur, min(cur+cost[i-1], pre+cost[i-2])
        return cur
        # dp = [cost[0], cost[1]]
        # for i in range(2, len(cost)):
        #     dp[i % 2] = min(dp[0], dp[1]) + cost[i]
        # return min(dp)
        # (1)
        # @lru_cache(None)
        # def dfs(i):
        #     if i < 0:
        #         return inf
        #     if i <= 1:
        #         return cost[i]
        #     return min(dfs(i-1), dfs(i-2)) + cost[i]
        # return min(dfs(len(cost)-1), dfs(len(cost)-2))
# @lc code=end

