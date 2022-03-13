#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start
from sortedcontainers import SortedDict


class MyCalendar:

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        after = self.calendar.bisect(start)
        if after < len(self.calendar) and self.calendar.values()[after] < end:
            return False
        self.calendar[end] = start
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

