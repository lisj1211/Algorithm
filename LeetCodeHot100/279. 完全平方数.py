# -*- coding: utf-8 -*-
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
# 示例1：
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/perfect-squares


class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))  # 每个数的初始值为n，n = 1 + 1 + ···+ 1
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # dp[i] = min(dp[i], dp[i - j * j] + dp[j * j]), dp[j * j] = 1
                if dp[i - j * j] + 1 < dp[i]:
                    dp[i] = dp[i - j * j] + 1
                j += 1

        return dp[-1]
