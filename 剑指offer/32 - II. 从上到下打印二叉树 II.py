# -*- coding: utf-8 -*-
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
#   [9,20],
#   [15,7]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof

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
            ans.append(tmp)
        return ans
