#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
# from sortedcontainers import SortedSet


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     buckets = {}
    #     for i, num in enumerate(nums):
    #         id = self.bucketId(num, t+1)
    #         if id in buckets or \
    #             (buckets.get(id+1) and buckets[id+1]<=num+t) or \
    #                 (buckets.get(id-1) and buckets[id-1]>=num-t):
    #             return True
    #         buckets[id] = num
    #         if i >= k:
    #             buckets.pop(self.bucketId(nums[i-k], t+1))
    #     return False

    # def bucketId(self, num, size):
    #     return num//size if num >= 0 else (num+1)//size-1
        sst = SortedSet()
        for i, num in enumerate(nums):
            lower = sst.bisect_right(num) -1
            if lower >= 0 and sst[lower] >= num - t:
                return True
            upper = sst.bisect_right(num)
            if upper < len(sst) and sst[upper] <= num + t:
                return True
            sst.add(num)
            if len(sst) > k:
                sst.remove(nums[i-k])
        return False
# @lc code=end

