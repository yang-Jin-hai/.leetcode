#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + digits
        # (2)
        # res = 0
        # for v in digits:
        #     res = 10*res + v
        # return [int(i) for i in str(res+1)]

        # (3)
        # carry, digits[-1]  = divmod(digits[-1]+1, 10)
        # if not carry: return digits
        # i = len(digits)-2
        # while carry and i>=0:
        #     carry, digits[i] = divmod(digits[i]+1, 10)
        #     i -= 1
        # if carry: return [1]+digits
        # return digits
# @lc code=end

