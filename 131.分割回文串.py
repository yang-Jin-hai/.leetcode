#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, m = [], len(s)
        @lru_cache(None)
        def valid(l, r):
            if l + 1 >= r:
                return s[l] == s[r]
            return valid(l+1, r-1) and s[l] == s[r]
        def dfs(index, last, path):
            if last == m:
                res.append(path[:])
                return
            if index > m:
                return
            dfs(index+1, last, path)
            if valid(last, index-1):
                dfs(index+1, index, path + [s[last:index]])
        dfs(1, 0, [])
        return res
# @lc code=end

