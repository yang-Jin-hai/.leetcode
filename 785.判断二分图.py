#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        m = len(graph)
        colors = m * [-1]
        def setColor(i, color):
            queue = deque([i])
            colors[i] = color
            while queue:
                cur = queue.popleft()
                for n in graph[cur]:
                    if colors[n] > -1:
                        if colors[cur] == colors[n]:
                            return False
                    else:
                        colors[n] = 1 - colors[cur]
                        queue.append(n)
            return True
        def setColor2(i, color):
            if colors[i] > -1:
                return colors[i] == color
            colors[i] = color
            for n in graph[i]:
                if not setColor2(n, 1-color):
                    return False
            return True
        for i in range(m):
            if colors[i] < 0:
                if not setColor(i, 0):
                    return False
        return True
# @lc code=end

