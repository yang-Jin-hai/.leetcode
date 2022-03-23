#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        lengths = [[1 for i in range(n)] for i in range(m)]
        def dfs(i, j):
            if lengths[i][j] > 1: return lengths[i][j]
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in dirs:
                _i, _j = i + d[0], j + d[1]
                if 0 <= _i < m and 0 <= _j < n and matrix[_i][_j] > matrix[i][j]:
                    lengths[i][j] = max(lengths[i][j], dfs(_i, _j) + 1)
            return lengths[i][j]
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
# @lc code=end

