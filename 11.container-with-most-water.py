#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    # def maxArea(self, height: List[int]) -> int:
        # low, high, max_area = 0, len(height)-1, 0
        # for width in range(high, 0, -1):
        #     max_area = max(min(height[low], height[high]) * width, max_area)
        #     if height[low] <= height[high]:
        #         low += 1
        #     else:
        #         high -= 1
        # return max_area
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res

# @lc code=end

