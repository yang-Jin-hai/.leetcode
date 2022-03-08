#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        negative = num < 0
        if negative:
            num = -num
        res = ''
        while num:
            num, val = divmod(num, 7)
            res = str(val) + res
        return '-' + res if negative else res
# @lc code=end

