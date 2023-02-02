# -*- coding: utf-8 -*-
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
#
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     / \     / \
#    7   2   5   1
# 示例 1：
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.f(root, [], target, ans)
        return ans

    def f(self, node, path, rest, ans):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and rest == node.val:
            ans.append(path.copy())
            # return  这里不能return, 因为return之后，当前节点还未pop，会对之后dfs产生影响

        self.f(node.left, path, rest - node.val, ans)
        self.f(node.right, path, rest - node.val, ans)
        path.pop()


# class Solution:
#     def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
#         if not root:
#             return []
#         ans = []
#         self.f(root, [], target, ans)
#         return ans
#
#     def f(self, node, path, rest, ans):
#         """
#         错误原因在于，当前逻辑为来到空节点时结算，因此当来到叶子节点时，会返回当前叶子节点2次，产生重复路径
#         """
#         if not node:
#             if rest == 0:
#                 ans.append(path.copy())
#             return
#         path.append(node.val)
#         self.f(node.left, path, rest - node.val, ans)
#         self.f(node.right, path, rest - node.val, ans)
#         path.pop()

