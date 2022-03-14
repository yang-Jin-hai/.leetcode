#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, m = [], len(candidates)
        def dfs(index, path, target):
            if target == 0:
                res.append(path[:])
                return
            if index == m or target < 0:
                return
            dfs(index+1, path, target)
            path.append(candidates[index])
            dfs(index, path, target-candidates[index])
            path.pop()
            return 
        dfs(0, [], target)
        return res
# @lc code=end

