#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        pre = self.generate(numRows=numRows-1)
        old = pre[-1]
        now = numRows * [1]
        for i in range(len(old)-1):
            now[i+1] = old[i] + old[i+1]
        pre.append(now)
        return pre

        # pascal = [[1]*(i+1) for i in range(numRows)]
        # for i in range(numRows):
        #     for j in range(1,i):
        #         pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        # return pascal
# @lc code=end

