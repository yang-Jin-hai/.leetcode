#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = len(edges)
        parents = list(range(m+1))
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parents[pi] = pj
                return True
        for i, j in edges:
            if not union(i, j):
                return [i, j]
# @lc code=end

