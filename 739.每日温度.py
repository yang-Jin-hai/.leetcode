#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        m = len(temperatures)
        res = m * [0]
        for i in range(m):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res
# @lc code=end

