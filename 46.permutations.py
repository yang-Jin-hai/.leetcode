#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(res, path, num):
            if not num:
                res.append(path)
                return 
            for i in range(len(num)):
                dfs(res, path+[num[i]], num[:i]+num[i+1:])
            return
        dfs(res, [], nums)
        return res
        # (1)
        # res = []
        # n = len(nums)
        # def dfs(start):
        #     if start == n:
        #         res.append(nums[:])
        #         return
        #     for i in range(start, n):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         dfs(start+1)
        #         nums[i], nums[start] = nums[start], nums[i]
        #     return
        # dfs(0)
        # return res
# @lc code=end

