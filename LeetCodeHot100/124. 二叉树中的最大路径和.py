# -*- coding: utf-8 -*-
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def f(node):
            # 以node为根节点的最大路径和
            if not node:
                return 0

            l = f(node.left)
            r = f(node.right)
            if l < 0:  # 负贡献
                l = 0
            if r < 0:
                r = 0
            if l + r + node.val > self.ans:
                self.ans = l + r + node.val

            return node.val + (r if l < r else l)

        f(root)
        return self.ans
