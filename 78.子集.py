#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, m = [], len(nums)
        def helpler(index, path):
            if index == m:
                res.append(path[:])
                return
            helpler(index+1, path)
            path.append(nums[index])
            helpler(index+1, path)
            path.pop()
            return
        helpler(0, [])
        return res
# @lc code=end

