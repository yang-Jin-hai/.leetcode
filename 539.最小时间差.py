#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        times = 1440 * [False]
        for time in timePoints:
            key = 60*int(time[:2]) + int(time[-2:])
            if times[key]:
                return 0
            times[key] = True
        minTime, maxTime, d = 1439, 0, 1439
        pre = -1
        for i in range(1440):
            if times[i]:
                if pre > 0:
                    d = min(d, i-pre)
                pre = i
                minTime, maxTime = min(minTime, i), max(maxTime, i)
        d = min(d, minTime-maxTime+1440)
        return d
# @lc code=end

