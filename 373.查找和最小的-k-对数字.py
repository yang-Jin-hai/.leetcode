#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[i]+nums2[0], i, 0) for i in range(min(len(nums1), k))]
        res = []
        while len(res) < k and heap:
            ids = heapq.heappop(heap)
            res.append([nums1[ids[1]], nums2[ids[2]]])
            if ids[2] < len(nums2)-1:
                heapq.heappush(heap, (nums1[ids[1]]+nums2[ids[2]+1], ids[1], ids[2]+1))
        return res
# @lc code=end

