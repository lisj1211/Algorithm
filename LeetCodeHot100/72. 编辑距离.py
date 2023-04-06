# -*- coding: utf-8 -*-
# 给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
# 示例1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/edit-distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for c in range(len(word2) + 1):
            dp[0][c] = c
        for r in range(len(word1) + 1):
            dp[r][0] = r

        for row in range(1, len(word1) + 1):
            for col in range(1, len(word2) + 1):
                if word1[row - 1] == word2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    # dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1] 分别代表替换，删除，插入
                    dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1

        return dp[-1][-1]
