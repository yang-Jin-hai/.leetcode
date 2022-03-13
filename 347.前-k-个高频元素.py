#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        heap = []
        for num in nums:
            counter[num] += 1
        for num, c in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, num))
            elif heap[0][0] < c:
                heapq.heappop(heap)
                heapq.heappush(heap, (c, num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
# @lc code=end

