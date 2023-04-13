# -*- coding: utf-8 -*-
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximal-rectangle
from pprint import pprint
from typing import List


class Solution:
    """对矩阵每一个位置，找到其左边连续1的数量，两点确定一个小矩阵，判断这个小矩阵是否都为1"""
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        left2right = [[0 for _ in range(n)] for _ in range(m)]  # 每一位置左边连续1的数量
        for row in range(m):
            sum_1 = 0
            for col in range(n):
                if matrix[row][col] == '1':
                    left2right[row][col] = sum_1 + 1
                    sum_1 += 1
                else:
                    sum_1 = 0

        ans = 0
        for top_i in range(m):
            for top_j in range(n):
                for bottom_i in range(top_i, m):
                    for bottom_j in range(top_j, n):
                        tmp = self.area(top_i, top_j, bottom_i, bottom_j, left2right)
                        if tmp > ans:
                            ans = tmp
        return ans

    def area(self, top_i, top_j, bottom_i, bottom_j, left2right):
        """以(top_i, top_j), (bottom_i, bottom_j)为左上角和右下角的矩阵面积"""
        for row in range(top_i, bottom_i + 1):
            if left2right[row][bottom_j] < bottom_j - top_j + 1:  # 每一行右端点其左边连续1的数量小于宽度，则存在0
                return 0
        return (bottom_j - top_j + 1) * (bottom_i - top_i + 1)


class Solution1:
    """可类比leetcode.84"""
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        left2right = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            sum_1 = 0
            for col in range(n):
                if matrix[row][col] == '1':
                    left2right[row][col] = sum_1 + 1
                    sum_1 += 1
                else:
                    sum_1 = 0
        ans = 0
        for col in range(n):
            lst = [left2right[row][col] for row in range(m)]
            area = self.max_area(lst)
            if area > ans:
                ans = area
        return ans

    def max_area(self, heights):
        if len(heights) == 1:
            return heights[0]

        heights = [0] + heights + [0]
        stack = [0]
        ans = 0
        for i in range(1, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                area = (i - stack[-1] - 1) * h
                if area > ans:
                    ans = area
            stack.append(i)
        return ans


s = Solution()
s.maximalRectangle(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]])
# (1, 2)
# (2, 4)
