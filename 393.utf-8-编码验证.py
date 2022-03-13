#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, m = 0, len(data)
        while i < m:
            num = data[i]
            if (num >> 7) & 1 == 0:
                i += 1
                continue
            else:
                bytes = self.getBytes(num)
                if not bytes or bytes <= 1 or bytes > 4: return False
                if i + bytes > m or not self.valid4Byte(data[i+1:i+bytes]):
                    return False
                i += bytes
        return True
    def getBytes(self, data):
        if data == 255: return False
        bytes, bit = 1, 6
        while bit >=0 and (data >> bit) & 1:
            bytes += 1
            bit -= 1
        return bytes
    def valid4Byte(self, data):
        for num in data:
            if num >> 6 != 2:
                return False
        return True
# @lc code=end

