#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#

# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def sim(x, y):
            c = 0
            for i, (xa, ya) in enumerate(zip(x, y)):
                if xa != ya:
                    c += 1
                    if c > 2:
                        return False
            return True
        res = m = len(strs)
        parents = list(range(m))
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi != pj:
                parents[pi] = pj
                return True
        for i, s in enumerate(strs):
            for j in range(i+1, m):
                if sim(s, strs[j]) and union(i, j):
                    res -= 1
        return res
# @lc code=end

