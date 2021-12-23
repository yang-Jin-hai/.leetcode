#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res[j] = res[j-1] + res[j] 
        return res

        # if rowIndex==0: return [1]
        # res = [1]*(rowIndex+1)
        # for i in range(2, rowIndex+1):
        #     old = res[:]
        #     for j in range(1, i):
        #         res[j] = old[j] + old[j-1] 
        # return res
# @lc code=end

