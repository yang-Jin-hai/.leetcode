#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) | isPalindrome(l, r-1)
            l += 1
            r -= 1
        return True

    
# @lc code=end

