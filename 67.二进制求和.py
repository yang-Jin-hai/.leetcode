#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = []
        if m < n: return self.addBinary(b, a)
        if b == '0': return a
        carry = 0
        for i in range(m):
            x = int(a[~i])
            if i < n:
                x += int(b[~i])
            x += carry
            x, carry = x & 1, x >> 1
            res.append(x)
        if carry: res.append(carry)
        return ''.join([str(i) for i in res[::-1]])
# @lc code=end

