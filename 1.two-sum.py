#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, v in enumerate(nums):
            if v in data:
                return [data[v], i]
            data[target-v] = i

# @lc code=end

