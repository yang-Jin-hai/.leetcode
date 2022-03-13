#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = 26 * [None]
        self.value = 0
    def insert(self, key, val):
        node = self
        for c in key:
            if node.children[ord(c)-ord('a')] == None:
                node.children[ord(c)-ord('a')] = Trie()
            node = node.children[ord(c)-ord('a')]
        node.value = val
    def search(self, key):
        node = self
        for c in key:
            if node.children[ord(c)-ord('a')] == None:
                return
            node = node.children[ord(c)-ord('a')]
        return node
    def dfs(self, root, res):
        if not root:
            return
        if root.value:
            res[0] += root.value
        if not any(root.children):
            return
        for child in root.children:
            self.dfs(child, res)
            
class MapSum:

    def __init__(self):
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        self.root.insert(key, val)

    def sum(self, prefix: str) -> int:
        res = [0]
        node = self.root.search(prefix)
        if not node: return 0
        self.root.dfs(node, res)
        return res[0]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

