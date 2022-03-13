#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
from sys import prefix


class Trie:
    def __init__(self):
        self.children = 26 * [None]
        self.is_word = False
    def insert(self, word):
        node = self
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = Trie()
                print(c)
            node = node.children[ord(c)-ord('a')]
        node.is_word = True
    def findPrefix(self, word):
        prefix = []
        node = self
        for c in word:
            if node.is_word:
                print(''.join(prefix))
                return ''.join(prefix)
            if node.children[ord(c)-ord('a')] == None:
                return
            prefix.append(c)
            node = node.children[ord(c)-ord('a')]
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        res = []
        for w in dictionary:
            root.insert(w)
        for w in sentence.split(' '):
            if (prefix:=root.findPrefix(w)) != None:
                res.append(prefix)
            else:
                res.append(w)
        return ' '.join(res)
# @lc code=end

