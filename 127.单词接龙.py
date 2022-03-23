#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getNeighbors(s):
            neighbors = []
            for i, c in enumerate(s):
                for j in range(26):
                    if c != chr(ord('a')+j):
                        neighbors.append(s[:i] + chr(ord('a')+j) + s[i+1:])
            return neighbors
        candidates = set(wordList)
        if endWord not in candidates: return 0
        set1 = set([beginWord])
        set2 = set([endWord])
        step = 2
        candidates.remove(endWord)
        while set1 and set2:
            set3 = set()
            if len(set1) > len(set2):
                set1, set2 = set2, set1
            for word in set1:
                neighbors = getNeighbors(word)
                for n in neighbors:
                    if n in set2: return step
                    if n in candidates:
                        set3.add(n)
                        candidates.remove(n)
            step += 1
            set1 = set3
        return 0
        # step = 1
        # candidates = set(wordList)
        # queue = deque([beginWord])
        # while queue:
        #     for i in range(len(queue)):
        #         word = queue.popleft()
        #         if word == endWord: return step
        #         neighbors = getNeighbors(word)
        #         for n in neighbors:
        #             if n in candidates:
        #                 queue.append(n)
        #                 candidates.remove(n)
        #     step += 1
        # return 0
# @lc code=end

