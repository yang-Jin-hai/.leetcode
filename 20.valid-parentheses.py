#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack, ps = [], {'(':')', '[':']', '{':'}'}
        for v in s:
            if v in ps:
                stack.append(v)
            elif not stack or v != ps[stack.pop()]:
                return False
        return not stack
# @lc code=end

