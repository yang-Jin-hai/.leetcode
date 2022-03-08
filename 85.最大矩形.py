#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = list(map(lambda x: int(x), matrix[0]))
        res = self.largerstArea(heights)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            print(heights)
            res = max(res, self.largerstArea(heights))
        return res

    def largerstArea(self, heights):
        m = len(heights)
        stack = [-1]
        res = 0
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

