#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start, end):
            pivot = random.randint(start, end)
            nums[pivot], nums[end] = nums[end], nums[pivot]
            small = start - 1
            for i in range(start, end):
                if nums[i] < nums[end]:
                    small += 1
                    nums[i], nums[small] = nums[small], nums[i]
            small += 1
            nums[small], nums[end] = nums[end], nums[small]
            return small
        l, r = 0, len(nums) - 1
        target = r - k + 1
        index = partition(l, r)
        while index != target:
            if index > target:
                r = index - 1
            else:
                l = index + 1
            index = partition(l, r)
        return nums[index]
# @lc code=end

