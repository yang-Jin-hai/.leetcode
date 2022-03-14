#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, m = [], len(candidates)
        candidates.sort()
        def dfs(index, target, path):
            if target == 0:
                res.append(path[:])
                return
            if index == m or target < 0:
                return  
            path.append(candidates[index])
            dfs(index+1, target-candidates[index], path)
            path.pop()
            while index < m - 1 and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, target, path)
        dfs(0, target, [])
        return res
# @lc code=end

