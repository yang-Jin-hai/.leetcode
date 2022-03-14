#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(index, path):
            if len(path) == k:
                res.append(path[:])
                return 
            if index > n:
                return
            dfs(index+1, path)
            path.append(index)
            dfs(index+1, path)
            path.pop()
            return
        dfs(1, [])
        return res
# @lc code=end

