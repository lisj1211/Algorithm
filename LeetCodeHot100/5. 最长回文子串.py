# -*- coding: utf-8 -*-
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = '#' + '#'.join(list(s)) + '#'
        left, right = 0, 0
        res = 1
        for i in range(len(s)):
            l, r = self.get_max_length(s, i)
            if r - l + 1 > res:
                res = r - l + 1
                left, right = l, r
        return s[left:right + 1].replace('#', '')

    def get_max_length(self, s, idx):
        """以idx位置为中心的最大回文子串边界"""
        length = len(s)
        i = j = idx
        while i >= 0 and j < length:
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break

        return i + 1, j - 1


class Solution1:
    """马拉车算法
    生成一个最大半径数组，每一元素表示当前位置最大回文串的半径
    L,R表示当前最右回文串的左右边界，C为其回文中心
    遍历填充后的字符串：
    1. 当前索引i在R的外部，暴力扩
    2. 分情况
        1)i关于C的对称位置i'的回文串范围在[L,R]内，i的最大回文长度即为i'的长度
        2)i关于C的对称位置i'的回文串范围一部分在[L,R]外，i的最大回文长度即为i'的长度
        3)i关于C的对称位置i'的回文串范围正好和[L,R]的左边界压线，则i的最大回文长度至少为i'的值，需要从R开始判断
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = '#' + '#'.join(list(s)) + '#'
        radius_lst = [0] * len(s)
        idx, ans = 0, 0
        R, C = -1, -1
        for i in range(len(s)):
            if i > R:  # 情况1
                l, r = self.get_max_length(s, i)
                R, C = r, i
                radius_lst[i] = R - C + 1
            else:  # 情况2
                i_prime = 2 * C - i
                i_prime_l, i_prime_r = i_prime - radius_lst[i_prime] + 1, i_prime + radius_lst[i_prime] - 1
                if i_prime_l > 2 * C - R:  # 情况2.1
                    radius_lst[i] = radius_lst[i_prime]
                elif i_prime_l < 2 * C - R:  # 情况2.2
                    radius_lst[i] = R - i + 1
                else:  # 情况2.3
                    while R + 1 < len(s) and s[R + 1] == s[2 * i - R - 1]:
                        R += 1
                        C = i
                    radius_lst[i] = R - i + 1
            if radius_lst[i] > ans:
                ans = radius_lst[i]
                idx = i
        return s[idx - radius_lst[idx] + 1:idx + radius_lst[idx] - 1].replace('#', '')

    def get_max_length(self, s, idx):
        length = len(s)
        i = j = idx
        while i >= 0 and j < length:
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break

        return i + 1, j - 1


class Solution2:
    """简洁版"""
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = '#' + '#'.join(list(s)) + '#'
        radius_lst = [0] * len(s)
        idx, ans = 0, 0
        R, C = -1, -1
        for i in range(len(s)):
            # i位置至少的回文区域
            radius_lst[i] = 1 if i > R else min(radius_lst[2 * C - i], R - i + 1)

            while i + radius_lst[i] < len(s) and s[i + radius_lst[i]] == s[i - radius_lst[i]]:
                radius_lst[i] += 1

            if i + radius_lst[i] - 1 > R:
                R = i + radius_lst[i] - 1
                C = i
            if radius_lst[i] > ans:
                ans = radius_lst[i]
                idx = i
        return s[idx - radius_lst[idx] + 1:idx + radius_lst[idx] - 1].replace('#', '')
