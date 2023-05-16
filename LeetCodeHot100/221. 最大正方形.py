# -*- coding: utf-8 -*-
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],
#                ["1","0","1","1","1"],
#                ["1","1","1","1","1"],
#                ["1","0","0","1","0"]]
# 输出：4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximal-square
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_size = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    max_size = 1 if max_size == 0 else max_size
                    limit = min(m - i, n - j)
                    for k in range(1, limit):
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break

                        for s in range(k):
                            if matrix[i + k][j + s] == '0' or matrix[i + s][j + k] == '0':
                                flag = False
                                break

                        if flag:
                            if k + 1 > max_size:
                                max_size = k + 1
                        else:
                            break
        return max_size * max_size


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        dp = [[0] * n for _ in range(m)]  # dp[i][j]表示以i,j位置为右下角的正方形的最大边长

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 左上角，左边，上边三者取较小
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    if dp[i][j] > ans:
                        ans = dp[i][j]

        return ans * ans


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    s = Solution()
    print(s.maximalSquare(matrix))
