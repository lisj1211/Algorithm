# -*- coding: utf-8 -*-
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        def f(node):
            if not node:
                return
            f(node.left)
            ans.append(node.val)
            f(node.right)

        f(root)
        return ans
