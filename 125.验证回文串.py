#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            sl, sr = s[l].lower(), s[r].lower()
            if not sl.isalnum():
                l += 1
                continue
            if not sr.isalnum():
                r -= 1
                continue
            if sl != sr:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

