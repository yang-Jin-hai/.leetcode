#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        m = len(nums)
        minStack, maxStack = [], []
        minLeft, maxLeft = m*[0], m*[0]
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)
            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minStack, maxStack = [], []
        minRight, maxRight = m*[0], m*[0]
        for i in range(m)[::-1]:
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else m
            minStack.append(i)
            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else m
            maxStack.append(i)

        minSum = maxSum = 0
        for i, num in enumerate(nums):
            minSum += num * (i - minLeft[i]) * (minRight[i] - i)
            maxSum += num * (i - maxLeft[i]) * (maxRight[i] - i)

        return maxSum - minSum

        
        # (1)
        # res, m = 0, len(nums)
        # for i in range(m):
        #     minV, maxV = 10**9, -10**9
        #     for j in range(i, m):
        #         minV = min(minV, nums[j])
        #         maxV = max(maxV, nums[j])
        #         res += maxV - minV
        # return res
# @lc code=end

