#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        res, m = [], len(s)
        @lru_cache(None)
        def valid(l, r):
            return len(s[l:r]) > 0 and int(s[l:r]) <= 255 and (s[l] != '0' or s[l:r] == '0')
        def dfs(index, n, path, last):
            if last == m and n == 4:
                res.append('.'.join(path))
                return
            if index > m:
                return
            dfs(index+1, n, path, last)
            if valid(last, index+1):
                dfs(index+1, n+1, path+[s[last:index+1]], index+1)
        dfs(0, 0, [], 0)
        return res
# @lc code=end

