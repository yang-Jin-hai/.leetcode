#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res, nums = [], {}
        m = 0
        for a, b in equations:
            if a not in nums:
                nums[a] = m
                m += 1
            if b not in nums:
                nums[b] = m
                m += 1
        graph = [[0 for i in range(m)] for i in range(m)]
        for i, (r, c) in enumerate(equations):
            r, c = nums[r], nums[c]
            graph[r][c] = values[i]
            graph[c][r] = 1 / values[i]
        def calc(query, visited):
            r, c = query
            if r == c: return 1.0
            if graph[r][c] != 0: return graph[r][c]
            visited.add(r)
            for n, v in enumerate(graph[r]):
                if v > 0 and n not in visited:
                    visited.add(n)
                    nxt = calc([n, c], visited)
                    if nxt > 0:
                        return graph[r][n] * nxt
            return - 1.0
        for query in queries:
            r, c = query
            if r not in nums or c not in nums: res.append(-1.0)
            else:
                res.append(calc([nums[i] for i in query], set([nums[query[0]]])))
        return res
# @lc code=end

