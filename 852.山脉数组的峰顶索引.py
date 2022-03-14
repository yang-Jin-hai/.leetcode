#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr)-2
        while l <= r:
            m = (l+r)>>1
            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif arr[m] <= arr[m-1]:
                r = m - 1
            else:
                l = m + 1
        return l
# @lc code=end

