# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(preorder: List[int], inorder: List[int]):
    if len(preorder) == 0:
        return None

    return recur(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def recur(preorder, prel, prer, inorder, inl, inr):
    """
    找到preorder范围[prel, prer]，inorder范围[inl, inr],构建出的头结点
    :param preorder: 先序序列
    :param prel: 先序序列左边界
    :param prer: 先序序列右边界
    :param inorder: 中序序列
    :param inl: 中序序列左边界
    :param inr: 中序序列右边界
    :return:
    """
    if prel > prer or inl > inr:  # 无法构建节点，返回None
        return None
    head = TreeNode(preorder[prel])  # 先序的第一个节点为头结点
    index = inorder.index(preorder[prel])  # 找到头结点在中序中的位置，左右部分即为左子树和右子树
    leftlen = index - inl  # 左子树的节点个数
    head.left = recur(preorder, prel + 1, prel + leftlen, inorder, inl, index - 1)
    head.right = recur(preorder, prel + leftlen + 1, prer, inorder, index + 1, inr)

    return head
