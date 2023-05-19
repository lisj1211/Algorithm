# -*- coding: utf-8 -*-
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        father_map = {root: None}

        def pre_order(node):
            if not node:
                return

            father_map[node.left] = node
            father_map[node.right] = node
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        node = p
        lst = set()
        while father_map[node] is not None:
            lst.add(node)
            node = father_map[node]

        node = q
        while father_map[node] is not None:
            if node in lst:
                return node
            node = father_map[node]

        return root


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if node == p or node == q or node is None:
                return node

            left = recur(node.left)
            right = recur(node.right)

            if left and right:
                return node

            return left if left else right

        return recur(root)
