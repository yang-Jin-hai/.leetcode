#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        begin, end = 0, len(numbers)-1
        while True:
            now = numbers[begin] + numbers[end]
            if now > target:
                end -= 1
            elif now < target:
                begin += 1
            else:
                return [begin+1, end+1]

        # hashtab = {}
        # for i, x in enumerate(numbers):
        #     if x in hashtab:
        #         return [hashtab[x]+1, i+1]
        #     hashtab[target-x] = i
# @lc code=end

