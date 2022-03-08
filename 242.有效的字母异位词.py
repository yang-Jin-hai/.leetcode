#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        hashtab = 26 * [0]
        for c in s:
            hashtab[ord(c)-ord('a')] += 1
        for c in t:
            if hashtab[ord(c)-ord('a')] == 0:
                return False
            hashtab[ord(c)-ord('a')] -= 1
        return True
        # return Counter(s) == Counter(t)
# @lc code=end

