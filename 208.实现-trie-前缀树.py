#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.children = 26 * [None]
        self.is_word = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = Trie()
            node = node.children[ord(c)-ord('a')]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                return False
            node = node.children[ord(c)-ord('a')]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if node.children[ord(c)-ord('a')] == None:
                return False
            node = node.children[ord(c)-ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

