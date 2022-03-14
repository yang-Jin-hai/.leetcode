#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        for num in arr2:
            res.extend(count[num]*[num])
            count.pop(num)
        l, r = -1, -1
        for num in count:
            l, r = min(l, num), max(r, num)
        for num in range(l, r+1):
            res.extend(count[num]*[num])
        return res
# @lc code=end

