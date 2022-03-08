#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [-1]
        m = len(heights)
        for i in range(m):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                cur = stack.pop()
                res = max(res, (i-stack[-1]-1)*heights[cur])
            stack.append(i)
        while stack[-1] != -1:
            cur = stack.pop()
            res = max(res, (m-stack[-1]-1)*heights[cur])
        return res
            
# @lc code=end

