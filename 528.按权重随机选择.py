#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        target = random.randint(0, self.w[-1]-1)
        l, r = 0, len(self.w)-1
        while l <= r:
            m = (l+r)>>1
            if self.w[m] > target:
                if m == 0 or self.w[m-1] <= target:
                    return m
                r = m - 1
            else:
                l = m + 1
        return 



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

