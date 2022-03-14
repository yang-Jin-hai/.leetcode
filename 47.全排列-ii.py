#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, m = [], len(nums)
        def dfs(i):
            if i == m:
                res.append(nums[:])
                return
            record = set()
            for j in range(i, m):
                if nums[j] in record:
                    continue
                record.add(nums[j])
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i+1)
                nums[j], nums[i] = nums[i], nums[j]
        dfs(0)
        return res
# @lc code=end

