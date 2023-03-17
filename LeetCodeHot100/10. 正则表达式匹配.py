# -*- coding: utf-8 -*-
# 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
#
# 示例 1：
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/regular-expression-matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == '.' or p[i - 1] == s[j - 1]:  # p[i]不为'*'时
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':  # p[i]为'*'时，需根据p[i-1]字符判断
                    if p[i - 2] != s[j - 1] and p[i - 2] != '.':  # 前一字符不相同
                        dp[i][j] = dp[i - 2][j]
                    else:  # 前一字符相同，则判断*匹配0,1和多个情况
                        dp[i][j] = dp[i - 2][j] or dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]
