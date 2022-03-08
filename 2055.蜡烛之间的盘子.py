#
# @lc app=leetcode.cn id=2055 lang=python3
#
# [2055] 蜡烛之间的盘子
#

# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res, m = len(queries) * [0], len(s)
        pre, nxt, counts = (m+1)*[0], (m+1)*[m], (m+1)*[0]
        for i in range(m):
            if s[i] == '|':
                counts[i+1] = counts[i] + 1
                pre[i+1] = i
            else:
                counts[i+1] = counts[i]
                pre[i+1] = pre[i]
        for i in range(m-1, -1, -1):
            if s[i] == '|':
                nxt[i] = i
            else:
                nxt[i] = nxt[i+1]
        for i, query in enumerate(queries):
            l, r = nxt[query[0]], pre[query[1]+1]
            if l < r:
                res[i] = r-l-(counts[r]-counts[l])
        return res
# @lc code=end

