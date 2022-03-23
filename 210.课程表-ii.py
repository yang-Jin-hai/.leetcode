#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = numCourses * [0]
        graph = [[] for  i in range(numCourses)]
        for i, o in prerequisites:
            inDegree[i] += 1
            graph[o].append(i)
        queue = deque()
        for i, v in enumerate(inDegree):
            if v == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for n in graph[course]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    queue.append(n)
        return res if len(res) == numCourses else []
# @lc code=end

