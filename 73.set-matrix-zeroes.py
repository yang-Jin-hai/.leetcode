#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = first_col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for j in range(m):
                matrix[j][0] = 0
        # (1)
        # m, n = len(matrix), len(matrix[0])
        # row, col = set(), set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row.add(i), col.add(j)
        # for i in row:
        #     for j in range(n):
        #         matrix[i][j] = 0
        # for i in col:
        #     for j in range(m):
        #         matrix[j][i] = 0
                
# @lc code=end

