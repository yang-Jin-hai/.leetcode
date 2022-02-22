#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        u, b, l, r = 0, n-1, 0, n-1
        v = 0
        while u <= b and r >= l:
            for i in range(l, r+1):
                v += 1
                res[u][i] = v
            u += 1
            for i in range(u, b+1):
                v += 1
                res[i][r] = v
            r -= 1
            for i in range(l, r+1)[::-1]:
                v += 1
                res[b][i] = v
            b -= 1
            for i in range(u, b+1)[::-1]:
                v += 1
                res[i][l] = v
            l += 1
        return res

# @lc code=end

