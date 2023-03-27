# -*- coding: utf-8 -*-
# 给你一个只包含 '('和 ')'的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-valid-parentheses


class Solution:
    """
    dp[i] 表示以i位置为结尾时最长有效括号子串的长度
    (1) dp[i] == '('，无法构成有效子串
    (2) dp[i] == ')'，需要看dp[i-1]位置的值
        1) dp[i-1] == '('，则dp[i-1]和dp[i]至少构成有效子串，还需看dp[i-2]的有效长度
        2) dp[i-1] == ')'，如果dp[i-1]存在有效子串，则需要看dp[i-1]之前的一个字符是否为'('，
        如果是，才能构成以i结尾的合法子串。另外还需看dp[i-1]之前的第二个字符的有效长度，
        例如`()(())`，当求以i=5位置时的最长有效子串dp[5]时，dp[4]=2，dp[2]='('，2-5构成有效子串，还需加dp[1]的值
    """
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(' or i == 0:
                continue

            if s[i - 1] == '(':
                dp[i] = 2 + dp[i - 2] if i - 2 >= 0 else 2
            else:
                if dp[i - 1] > 0 and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2
                if i - dp[i] >= 0:
                    dp[i] += dp[i - dp[i]]
            if dp[i] > ans:
                ans = dp[i]

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()"))
