# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
# https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []
        tr, tc, br, bc = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        ans = []
        while tr <= br and tc <= bc:
            ans.extend(self.clockwise(matrix, tr, tc, br, bc))
            tr += 1
            tc += 1
            br -= 1
            bc -= 1

        return ans

    def clockwise(self, matrix, tr, tc, br, bc):
        if tr == br:
            return matrix[tr][tc: bc + 1]
        if tc == bc:
            return [matrix[row][tc] for row in range(tr, br + 1)]

        lst = []
        for i in range(tc, bc):
            lst.append(matrix[tr][i])
        for i in range(tr, br):
            lst.append(matrix[i][bc])
        for i in range(bc, tc, -1):
            lst.append(matrix[br][i])
        for i in range(br, tr, -1):
            lst.append(matrix[i][tc])

        return lst

