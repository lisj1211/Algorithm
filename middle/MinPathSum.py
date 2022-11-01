# -*- coding: utf-8 -*-
# 给你一个二维数组matrix，其中每个数都是正数，要求从左上角走到右下角。每一步只能向右或者向下，沿途经过的数字要累加起来。最后请返回最小的路径和。


def min_path(matrix):
    row, col = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]

    dp[0][0] = matrix[0][0]  # dp[i][j]表示从左和从上方到当前位置的最小路径和
    for i in range(1, col):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]
    for i in range(1, row):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

    return dp[-1][-1]


def min_path1(matrix):
    """
    空间压缩，由于更新过程只依赖当前位置的上侧和左侧值，所以可以只用一个列表进行更新
    :param matrix:
    :return:
    """
    row, col = len(matrix), len(matrix[0])
    more = max(row, col)
    less = min(row, col)
    row_more = True if row > col else False
    dp = [0] * less  # 因为行列长度可能差距很大，所以选择较小的值进行初始化(比如有100万行，5列，则构建维度为5的列表进行更新)
    dp[0] = matrix[0][0]
    for i in range(1, less):
        dp[i] = dp[i - 1] + (matrix[0][i] if row_more else matrix[i][0])  # 判断行数多还是列数多

    for i in range(1, more):
        dp[0] += matrix[i][0] if row_more else matrix[0][i]  # 当前未更新的dp值代表上一层的值
        for j in range(1, less):
            dp[j] = min(dp[j - 1], dp[j]) + (matrix[i][j] if row_more else matrix[j][i])

    return dp[-1]


if __name__ == '__main__':
    matrix = [[1, 3, 5, 9],
              [8, 1, 3, 4],
              [5, 0, 6, 1],
              [8, 8, 4, 0]]
    print(min_path(matrix))
    print(min_path1(matrix))
