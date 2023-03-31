# -*- coding: utf-8 -*-
# 给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/rotate-image
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left_r, left_c, right_r, right_c = 0, 0, len(matrix) - 1, len(matrix) - 1
        while left_r <= right_r:  # 一圈一圈交换，left_r和left_c相等，可以进行优化
            self.f(matrix, left_r, left_c, right_r, right_c)
            left_r += 1
            left_c += 1
            right_r -= 1
            right_c -= 1
        return

    def f(self, matrix, left_r, left_c, right_r, right_c):
        """交换每一圈的n个值"""
        if left_r == right_r:
            return
        tmp_list = matrix[left_r][left_c:right_c]  # 每次交换一整行或一整列交换
        for i, r in zip(range(len(tmp_list)), range(left_r, right_r)):
            tmp_list[i], matrix[r][right_c] = matrix[r][right_c], tmp_list[i]
        for i, c in zip(range(len(tmp_list)), range(right_c, left_c, -1)):
            tmp_list[i], matrix[right_r][c] = matrix[right_r][c], tmp_list[i]
        for i, r in zip(range(len(tmp_list)), range(right_r, left_r, -1)):
            tmp_list[i], matrix[r][left_c] = matrix[r][left_c], tmp_list[i]
        for i, c in zip(range(len(tmp_list)), range(left_c, right_c)):
            tmp_list[i], matrix[left_r][c] = matrix[left_r][c], tmp_list[i]


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        left_idx, right_idx = 0, len(matrix) - 1
        while left_idx <= right_idx:
            for i in range(right_idx - left_idx):
                # 每次交换4个方向中的一个值
                matrix[left_idx][left_idx + i], matrix[left_idx + i][right_idx], matrix[right_idx][right_idx - i], matrix[right_idx - i][left_idx] = \
                    matrix[right_idx - i][left_idx], matrix[left_idx][left_idx + i], matrix[left_idx + i][right_idx], matrix[right_idx][right_idx - i]
            left_idx += 1
            right_idx -= 1
        return