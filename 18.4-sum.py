#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        def findNsum(low, high, N, result, results, target):
            if N < 2 or high-low+1 < N or N*nums[low] > target or N*nums[high] < target:
                return
            if N == 2:
                while low<high:
                    s = nums[low] + nums[high]
                    if s == target:
                        results.append(result + [nums[low], nums[high]])
                        low += 1
                        while low<high and nums[low] == nums[low-1]:
                            low += 1
                    elif s > target:
                        high -= 1
                    else:
                        low += 1
            else:
                for i in range(low, high+1):
                    if i == low or nums[i-1] != nums[i]:
                        findNsum(i+1, high, N-1, result+[nums[i]], results, target-nums[i])

        findNsum(0, len(nums)-1, 4, [], results, target)
        return results

# @lc code=end

