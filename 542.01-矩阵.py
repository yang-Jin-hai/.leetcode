#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[inf for i in range(n)] for i in range(m)]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    res[i][j] = 0
        while queue:
            i, j = queue.popleft()
            dist = res[i][j]
            for d in dirs:
                r, c = i + d[0], j + d[1]
                if r >= 0 and r < m and c >= 0 and c < n and res[r][c] > dist+1:
                    queue.append([r, c])
                    res[r][c] = dist + 1
        return res
# @lc code=end

