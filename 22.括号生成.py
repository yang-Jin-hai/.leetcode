#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(i, path, l, r):
            if i == n << 1 and l == r == n:
                res.append(path[:])
                return
            if l > n or r > n or i > n << 1 or l < r:
                return
            dfs(i+1, path, l, r)
            dfs(i+1, path+'(', l+1, r)
            dfs(i+1, path+')', l, r+1)
        dfs(0, '', 0, 0)
        return res
# @lc code=end

