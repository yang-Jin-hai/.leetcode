#
# @lc app=leetcode.cn id=676 lang=python3
#
# [676] 实现一个魔法字典
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = 26 * [None]
        self.is_word = False
    def insert(self, word):
        node = self
        for c in word:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = Trie()
            node = node.children[ord(c)-ord('a')]
        node.is_word = True
    def search(self, root, word, i, edit):
        if not root: return False
        if root.is_word and i==len(word) and edit==1:
            return True
        if i < len(word) and edit <= 1:
            found = False
            for j in range(26):
                next = edit + 1 if ord(word[i]) - ord('a') != j else edit
                found = self.search(root.children[j], word, i+1, next)
                if found: return True
            return False
        return False

class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.root.insert(w)

    def search(self, searchWord: str) -> bool:
        return self.root.search(self.root, searchWord, 0, 0)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end

