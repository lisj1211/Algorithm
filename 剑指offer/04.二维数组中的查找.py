# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
#
# 输入：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。
from typing import List


# 方法一：暴力寻找
def find_number_in_2d_array(matrix: List[List[int]], target: int):
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == target:
                return True

    return False


# 方法二： 根据条件
def find_number_in_2d_array1(matrix: List[List[int]], target: int):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    row, col = len(matrix) - 1, 0  # 左下角元素
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:  # 如果左下角元素大于target，则该行所有元素均大于target
            row -= 1
        else:  # 如果左下角元素小于target，则该列所有元素均小于target
            col += 1

    return False

