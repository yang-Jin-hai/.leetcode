#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = 26 * [None]
    def insert(self, word):
        node = self
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = Trie()
                print(c)
            node = node.children[ord(c)-ord('a')]
    def dfs(self, root, res, path):
        isLeaf = True
        for child in root.children:
            if child is not None:
                isLeaf = False
                self.dfs(child, res, path+1)
        if isLeaf: 
            print(res[0])
            res[0] += path

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Trie()
        for w in words:
            root.insert(w[::-1])
        res = [0]
        root.dfs(root, res, 1)
        return res[0]
# @lc code=end

