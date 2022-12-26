# -*- coding: utf-8 -*-
# 已知一棵二叉树中没有重复节点，并且给定了这棵树的中序遍历数组和先序遍历数组，返回后序遍历数组。
# 比如给定：
# pre = [ 1, 2, 4, 5, 3, 6, 7 ]
# in = [4, 2, 5, 1, 6, 3, 7 ]
# 返回：
# [4,5,2,6,7,3,1]
from typing import List


def get_post_order(pre_order: List[int], in_order: List[int]) -> List[int]:
    if not pre_order or not in_order:
        return []
    post_order = [0] * len(pre_order)
    fill(pre_order, 0, len(pre_order) - 1, in_order, 0, len(in_order) - 1, post_order, 0, len(post_order) - 1)

    return post_order


def fill(pre_order, pre_l, pre_r, in_order, in_l, in_r, post_order, post_l, post_r):
    if pre_l > pre_r:
        return

    head = pre_order[pre_l]  # 头结点
    post_order[post_r] = head  # 放到后序列表的末尾
    head_indx = in_order.index(head)  # 根据头结点将中序列表一分为二，递归填写左右部分，此处可以用字典加速查找过程
    # left_len = head_indx - in_l
    fill(pre_order, pre_l + 1, pre_l + head_indx - in_l, in_order, in_l, head_indx - 1,
         post_order, post_l, post_l + head_indx - in_l - 1)

    fill(pre_order, pre_l + 1 + head_indx - in_l, pre_r, in_order, head_indx + 1, in_r,
         post_order, post_l + head_indx - in_l, post_r - 1)


if __name__ == '__main__':
    pre_ = [1, 2, 4, 5, 3, 6, 7]
    in_ = [4, 2, 5, 1, 6, 3, 7]
    print(get_post_order(pre_, in_))
