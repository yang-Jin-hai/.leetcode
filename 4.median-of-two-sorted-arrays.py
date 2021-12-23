#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high, all = 0, m, (m + n - 1) >> 1
        while low < high:
            i = (low + high) >> 1
            if all-i-1 < 0 or nums1[i] >= nums2[all-i-1]:
                high = i
            else:
                low = i + 1
        mids = sorted(nums1[low:low+2] + nums2[all-low:all-low+2])
        if (m+n) %2:
            return mids[0]
        return (mids[0] + mids[1]) / 2

# @lc code=end

