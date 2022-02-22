#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res, mask, n = 0, 1, len(nums)
        # for i in range(32):
        #     c = 0
        #     for num in nums:
        #         if mask & num:
        #             c += 1
        #     if c > n / 2:
        #         res |= mask
        #     mask = mask << 1
        # return res
        # (2)
        res, c = nums[0], 0
        for x in nums:
            if x == res:
                c += 1
            elif c == 0:
                res, c = x, 1
            else:
                c -= 1
        return res
        # (1)
        # c = Counter(nums)
        # return c.most_common(1)[0][0]
# @lc code=end

