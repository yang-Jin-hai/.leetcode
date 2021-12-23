#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and not x%10): return False
        y = 0
        while x > y:
            x, r = divmod(x, 10)
            if x == y: 
                return True 
            y = 10*y + r
        return x == y
        
        # if x < 0: return False
        # x = str(x)
        # return x==x[::-1]

        # y, z = 0, x
        # while z>0:
        #     z, r = divmod(z, 10)
        #     y = 10*y + r
        # return x == y

# @lc code=end

