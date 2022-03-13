#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        prev = None
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev:
                prev.right = cur
            else:
                first = cur
            prev = cur
            cur.left = None
            cur = cur.right
        return first
        # (1)
        # queue = deque()
        # def dfs(root):
        #     if not root: return
        #     dfs(root.left)
        #     queue.append(TreeNode(root.val))
        #     dfs(root.right)
        #     return
        # dfs(root)
        # root = cur = queue.popleft()
        # while queue:
        #     cur.right = queue.popleft()
        #     cur = cur.right
        # return root
# @lc code=end

