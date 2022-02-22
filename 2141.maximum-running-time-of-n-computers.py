#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
import bisect


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries = sorted(batteries, reverse=True)
        sumt = sum(batteries)
        for x in batteries:
            if x > sumt // n:
                sumt -= x
                n -= 1
            else:
                return sumt // n
        # (2)
        # l, r = 0, sum(batteries) // n
        # batteries.sort()
        # m = len(batteries)
        # while l <= r:
        #     mid = (l + r) >> 1
        #     sep = bisect.bisect(batteries, mid)
        #     cap = (m-sep) * mid
        #     for i in range(sep):
        #         cap += batteries[i]
        #     if cap >= mid * n:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r
        # (1)
        # l, r = 0, sum(batteries) // n
        # batteries.sort()
        # m = len(batteries)
        # pre = [0]
        # for i in batteries:
        #     pre.append(pre[-1]+i)
        # while l <= r:
        #     mid = (l + r) >> 1
        #     sep = bisect.bisect(batteries, mid)
        #     cap = (m-sep) * mid + pre[sep]
        #     if cap >= mid * n:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return r
# @lc code=end

