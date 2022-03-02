#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        target, odd = (m + n + 1) >> 1, (m + n) & 1
        l, r = 0, m
        while l <= r:
            mid1 = (l + r) >> 1
            mid2 = target - mid1
            if mid1 < m and nums1[mid1] < nums2[mid2-1]:
                l = mid1 + 1
            elif mid1 > 0 and nums1[mid1-1] > nums2[mid2]:
                r = mid1 - 1
            else:
                if mid1 == 0:
                    left_max = nums2[mid2-1]
                elif mid2 == 0:
                    left_max = nums1[mid1-1]
                else:
                    left_max = max(nums1[mid1-1], nums2[mid2-1])
                if odd:
                    return left_max
                if mid1 == m:
                    right_min = nums2[mid2]
                elif mid2 == n:
                    right_min = nums1[mid1]
                else:
                    right_min = min(nums2[mid2], nums1[mid1])
                return (left_max + right_min) / 2 

# @lc code=end

