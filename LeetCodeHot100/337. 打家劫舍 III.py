# -*- coding: utf-8 -*-
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为root。
#
# 除了root之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
# 聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
#
# 给定二叉树的root。返回在不触动警报的情况下，小偷能够盗取的最高金额。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/house-robber-iii
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def recur(node: TreeNode):
            if not node:
                return 0, 0
            l1, l2 = recur(node.left)
            r1, r2 = recur(node.right)

            return node.val + l2 + r2, max(l1, l2) + max(r1, r2)
        s1, s2 = recur(root)

        return s1 if s1 > s2 else s2