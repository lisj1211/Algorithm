# -*- coding: utf-8 -*-
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/validate-binary-search-tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """中序遍历"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []

        def f(node):
            if not node:
                return
            f(node.left)
            lst.append(node.val)
            f(node.right)

        f(root)
        for i in range(1, len(lst)):
            if lst[i] <= lst[i - 1]:
                return False

        return True


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.f(root, float('-inf'), float('inf'))

    def f(self, node, lower, upper):
        """判断以node为根节点的树是否在（lower, upper）范围内"""
        if not node:
            return True

        if lower < node.val < upper:
            return self.f(node.left, lower, node.val) and self.f(node.right, node.val, upper)

        return False

