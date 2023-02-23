# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        for n in range(1, len(grid[0])):
            grid[0][n] += grid[0][n - 1]
        for m in range(1, len(grid)):
            grid[m][0] += grid[m - 1][0]

        for m in range(1, len(grid)):
            for n in range(1, len(grid[0])):
                grid[m][n] += max(grid[m - 1][n], grid[m][n - 1])

        return grid[-1][-1]
