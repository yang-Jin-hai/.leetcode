#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        def sim(a, b):
            return a - b == 1 or b - a == 1
        nums = list(set(nums))
        m = len(nums)
        parents = list(range(m))
        counts = [1 for i in range(m)]
        nums.sort()
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parents[pi] = pj
                counts[pj] += counts[pi]
                return True
        for i in range(1, m):
            if sim(nums[i], nums[i-1]):
                union(i-1, i)
        return max(counts)
# @lc code=end

