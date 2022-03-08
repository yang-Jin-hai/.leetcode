#
# @lc app=leetcode.cn id=2100 lang=python3
#
# [2100] 适合打劫银行的日子
#

# @lc code=start
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        m = len(security)
        increase = [0] * m
        decrease = [0] * m
        for i in range(1, m):
            if security[~i] <= security[~(i-1)]:
                increase[~i] = increase[~(i-1)] + 1
            if security[i] <= security[i-1]:
                decrease[i] = decrease[i-1] + 1
        return [i for i in range(m) if increase[i]>= time and decrease[i]>=time]
# @lc code=end

