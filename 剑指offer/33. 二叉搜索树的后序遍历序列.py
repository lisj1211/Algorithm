# -*- coding: utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回true，否则返回false。
# 假设输入的数组的任意两个数字都互不相同。
#
# 参考以下这颗二叉搜索树：
#
#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：
#
# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：
#
# 输入: [1,3,2,6,5]
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        return self.is_BST(postorder, 0, len(postorder) - 1)

    def is_BST(self, postorder, left, right):
        """后续遍历列表最后一个数即为根节点
        【Error】：在找到第一个大于根节点的值，下意识用了二分查找，但是二分查找要求列表有序，导致调试了一阵子。
        """
        if left >= right:
            return True
        p = left
        while postorder[p] < postorder[right]:  # 找到第一个大于根节点的值，左侧为左子树，右侧为右子树
            p += 1
        for i in range(p, right):  # 右侧列表，即右子树的值都必须大于根节点值
            if postorder[i] < postorder[right]:
                return False

        return self.is_BST(postorder, left, p - 1) and self.is_BST(postorder, p, right - 1)
