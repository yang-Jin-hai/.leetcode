#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while u <= b and l <= r:
            for i in range(l, r+1):
                res.append(matrix[u][i])
            u += 1
            for i in range(u, b+1):
                res.append(matrix[i][r])
            r -= 1
            if u <= b:
                for i in range(l, r+1)[::-1]:
                    res.append(matrix[b][i])
            b -= 1
            if l <= r:
                for i in range(u, b+1)[::-1]:
                    res.append(matrix[i][l])
            l += 1
        return res

# @lc code=end

