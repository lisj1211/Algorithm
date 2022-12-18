# -*- coding: utf-8 -*-
# 给定一个整型矩阵，返回子矩阵的最大累计和。
# 思路：固定行，即只包含第一行的最大矩阵和，只包含第一，二行的最大矩阵和，依次求出。求只包含第一行的最大矩阵和，即求
# 第一行的最大子数组和；求包含第一，二行的最大矩阵和时，求lst = matrix[0] + matrix[1] 的最大子数组和。
from typing import List


def max_sum_in_matrix(matrix: List[List[int]]) -> int:
    row, col = len(matrix), len(matrix[0])
    max_ = float('-inf')
    for i in range(row):
        lst = [0] * col
        for j in range(i, row):
            pre = 0
            for k in range(col):
                lst[k] += matrix[j][k]
                if pre < 0:
                    pre = lst[k]
                else:
                    pre += lst[k]
                max_ = max(pre, max_)

    return max_


if __name__ == '__main__':
    mat = [[-90, 48, 78],
           [64, -40, 64],
           [-81, -7, 66]]
    print(max_sum_in_matrix(mat))
