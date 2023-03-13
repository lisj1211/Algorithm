# -*- coding: utf-8 -*-
# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        start = -1
        dic = {}
        for idx, ch in enumerate(s):
            if ch in dic:
                start = max(start, dic[ch])
            if idx - start > ans:
                ans = idx - start
            dic[ch] = idx
        return ans


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dic = set()
        ans = 0
        left = 0
        for idx, ch in enumerate(s):
            if ch in dic:
                while ch in dic:
                    dic.remove(s[left])
                    left += 1
            dic.add(ch)
            if idx - left + 1 > ans:
                ans = idx - left + 1
        return ans
