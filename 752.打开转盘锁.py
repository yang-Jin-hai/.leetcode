#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNeighbors(s):
            neighbors = []
            for i in range(4):
                neighbors.append(s[:i] + str((int(s[i])-1)%10) + s[i+1:])
                neighbors.append(s[:i] + str((int(s[i])+1)%10) + s[i+1:])
            return neighbors
        if '0000' in deadends: return -1
        if '0000' == target: return 0
        set1, set2 = set(["0000"]), set([target])
        visited = set(["0000", target])
        step = 1
        while set1 and set2:
            if len(set2) < len(set1): set1, set2 = set2, set1
            set3 = set()
            for code in set1:
                neighbor = getNeighbors(code)
                for n in neighbor:
                    if n not in deadends:
                        if n in set2:
                            return step
                        if n not in visited:
                            set3.add(n)
                            visited.add(n)
            step += 1
            set1 = set3
        return -1
        # if '0000' in deadends: return -1
        # if '0000' == target: return 0
        # queue = deque(['0000'])
        # visited = set(['0000'])
        # res = 1
        # while queue:
        #     for i in range(len(queue)):
        #         code = queue.popleft()
        #         neighbors = getNeighbors(code)
        #         for n in neighbors:
        #             if n not in visited and n not in deadends:
        #                 if n == target:
        #                     return res
        #                 else:
        #                     queue.append(n)
        #                     visited.add(n)
        #     res += 1
        # return -1
# @lc code=end

