#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(graph)
        def dfs(i, path):
            path += [i]
            if i == m - 1:
                res.append(path[:])
                return
            for n in graph[i]:
                dfs(n, path[:])
        dfs(0, [])
        return res
# @lc code=end

