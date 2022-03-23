#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for value in coins:
                if i >= value:
                    dp[i] = min(dp[i], dp[i-value]+1)
        return dp[-1] if dp[-1] <= amount else -1
        # m = len(coins)
        # dp = [amount+1] * (amount+1)
        # dp[0] = 0
        # for value in coins:
        #     for j in range(1, amount+1)[::-1]:
        #         k = 1
        #         while k * value <= j:
        #             dp[j] = min(dp[j], dp[j-k*value]+k)
        #             k += 1
        # return dp[-1] if dp[-1] <= amount else -1
# @lc code=end

