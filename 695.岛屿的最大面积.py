#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for i in range(m)]
        res = 0
        def area(i, j):
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            a = 1
            for d in dirs:
                _i, _j = i + d[0], j + d[1]
                if _i >= 0 and _i < m and _j >= 0 and _j < n and grid[_i][_j] and not visited[_i][_j]:
                    visited[_i][_j] = True
                    a += area(_i, _j)
            return a
        def area2(i, j):
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            a = 0
            queue = deque([[i, j]])
            visited[i][j] = True
            while queue:
                a += 1
                i, j = queue.pop()
                for d in dirs:
                    _i, _j = i + d[0], j + d[1]
                    if _i >= 0 and _i < m and _j >= 0 and _j < n and grid[_i][_j] and not visited[_i][_j]:
                        queue.append([_i, _j])
                        visited[_i][_j] = True
            return a

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    res = max(res, area2(i, j))
        return res
# @lc code=end

