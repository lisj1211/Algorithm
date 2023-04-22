# -*- coding: utf-8 -*-
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None, None
        left_h, left_t = self.flatten(root.left)
        right_h, right_t = self.flatten(root.right)
        root.left = None  # 左指针需要置空
        if left_h:
            root.right = left_h
            left_t.right = right_h
        else:
            root.right = right_h

        return root, right_t if right_t else (left_t if left_t else root)