#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, m = [], len(nums)
        def dfs(i):
            if i == m:
                res.append(nums[:])
                return
            for j in range(i, m):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[j], nums[i] = nums[i], nums[j]
        dfs(0)
        return res
# @lc code=end

