# -*- coding: utf-8 -*-
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-path-sum/?favorite=2cktkvj
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, m):
            for col in range(1, n):
                min_ = dp[row - 1][col] if dp[row - 1][col] < dp[row][col - 1] else dp[row][col - 1]
                dp[row][col] = min_ + grid[row][col]

        return dp[-1][-1]