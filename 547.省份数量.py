#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        res = m
        parents = list(range(m))
        def get_parents(i):
            if parents[i] != i:
                parents[i] = get_parents(parents[i])
            return parents[i]
        def union(i, j):
            pi = get_parents(i)
            pj = get_parents(j)
            if pi != pj:
                parents[pi] = pj
                return True
        for i in range(m):
            for j in range(i+1, m):
                if isConnected[i][j] and union(i, j):
                    res -= 1
        return res
        # res = 0
        # m = len(isConnected)
        # visited = [False for i in range(m)]
        # def dfs(i):
        #     visited[i] = True
        #     for j, v in enumerate(isConnected[i]):
        #         if v and not visited[j]:
        #             dfs(j)
        # for i in range(m):
        #     if not visited[i]:
        #         dfs(i)
        #         res += 1
        # return res
# @lc code=end

