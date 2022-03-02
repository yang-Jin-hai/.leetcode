#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        m = len(s)
        res = ''
        if m <= numRows or numRows == 1:
            return s
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                res += s[row::2*numRows-2]
            else:
                l1 = row
                l2 = 2 * numRows - row - 2
                stride = 2 * (numRows-1)
                while l1 < m or l2 < m:
                    if l1 < m:
                        res += s[l1]
                        l1 += stride
                    if l2 < m:
                        res += s[l2]
                        l2 += stride 
        return res
        # (1)
        # if len(s) <= numRows or numRows == 1:
        #     return s
        # res = [''] * numRows
        # index, dir = 0, 1
        # for x in s:
        #     res[index] += x
        #     if index == numRows-1:
        #         dir = -1
        #     elif index == 0:
        #         dir = 1
        #     index += dir
        # return ''.join(res)
            
# @lc code=end

