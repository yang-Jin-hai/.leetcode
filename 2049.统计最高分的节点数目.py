#
# @lc app=leetcode.cn id=2049 lang=python3
#
# [2049] 统计最高分的节点数目
#

# @lc code=start
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        m = len(parents)
        children = [[] for _ in range(m)]
        maxval, c = 0, 0
        for node, parent in enumerate(parents[1:], 1):
            children[parent].append(node)
        def dfs(root):
            score, size = 1, m - 1
            for child in children[root]:
                child_size = dfs(child)
                score *= child_size
                size -= child_size
            if root > 0: score *= size
            nonlocal maxval, c
            if score > maxval:
                maxval, c = score, 1
            elif score == maxval:
                c += 1
            return m - size
        dfs(0)
        return c 
# @lc code=end

