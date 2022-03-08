#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        self.values = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.values:
            remove_idx = self.values[val]
            self.nums[-1], self.nums[remove_idx] = self.nums[remove_idx], self.nums[-1]
            self.values[self.nums[remove_idx]] = remove_idx
            self.nums.pop()
            self.values.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

