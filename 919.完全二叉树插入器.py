#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque([root])
        while self.queue[0].left and self.queue[0].right:
            node = self.queue.popleft()
            self.queue.append(node.left)
            self.queue.append(node.right)
        if self.queue[0].left:
            self.queue.append(self.queue[0].left)


    def insert(self, val: int) -> int:
        parent = self.queue[0]
        node = TreeNode(val)
        if parent.left:
            self.queue.popleft()
            parent.right = node
            self.queue.append(node)
            # self.queue.append(parent.right)
        else:
            parent.left = node
            self.queue.append(node)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end

