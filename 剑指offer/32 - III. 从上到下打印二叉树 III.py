# -*- coding: utf-8 -*-
# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，
# 第三行再按照从左到右的顺序打印，其他行以此类推。
#
# 例如:
# 给定二叉树:[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        flag = 1
        ans = []
        queue = deque([root])
        while queue:
            tmp = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not flag:
                tmp.reverse()
            ans.append(tmp)
            flag = 1 - flag
        return ans
