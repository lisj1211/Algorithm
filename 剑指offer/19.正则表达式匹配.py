# 给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/regular-expression-matching


def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):  # 匹配空串
        if p[i - 1] == '*':
            dp[0][i] = dp[0][i - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] != '*':
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':  # p[j - 1] 与 s[i - 1] 字符匹配
                    dp[i][j] = dp[i - 1][j - 1]
            else:
                if p[j - 2] != s[i - 1] and p[j - 2] != '.':  # p[j - 2] 与 s[i - 1] 字符不匹配
                    dp[i][j] = dp[i][j - 2]
                else:  # p[j - 2] 与 s[i - 1] 字符匹配，匹配0个，匹配1个，匹配多个
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]

    return dp[m][n]


if __name__ == '__main__':
    print(is_match("aa", 'a'))
