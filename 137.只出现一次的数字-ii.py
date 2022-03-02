#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bits = 0
            for num in nums:
                bits += (num >> i) & 1
            if bits % 3:
                if i == 31:
                    res -= 2 ** 31
                else:
                    res |= 1 << i
        return res

        # (1)
        # bits = [0] * 32
        # for num in nums:
        #     for i in range(32):
        #         bits[~i] += (num >> i)  & 1
        # res = 0
        # for i, bit in enumerate(bits):
        #     if i == 0:
        #         res = (res << 1) - bit % 3
        #     else:
        #         res = (res << 1) + bit % 3
        # return res
# @lc code=end

