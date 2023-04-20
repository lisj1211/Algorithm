# -*- coding: utf-8 -*-
# 给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，
# 请构造二叉树并返回其根节点。
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_l, pre_r, inorder, in_l, in_r):
        if pre_l == pre_r:
            return TreeNode(preorder[pre_l])
        if pre_l > pre_r:
            return None
        val = preorder[pre_l]
        root = TreeNode(val)
        idx = inorder.index(val)

        root.left = self.build(preorder, pre_l + 1, pre_l + idx - in_l, inorder, in_l, idx - 1)
        root.right = self.build(preorder, pre_l + idx - in_l + 1, pre_r, inorder, idx + 1, in_r)
        return root
