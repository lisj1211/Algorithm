# -*- coding: utf-8 -*-
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/word-break
from typing import List


class Solution:
    """超时"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return True

        ans = False
        for word in wordDict:
            if s[:len(word)] == word:
                ans = ans or self.wordBreak(s[len(word):], wordDict)
        return ans


class Solution1:
    """通过！"""
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        import functools

        @functools.lru_cache(None)
        def f(s):
            if s == '':
                return True

            ans = False
            for word in wordDict:
                if s[:len(word)] == word:
                    ans = ans or f(s[len(word):])
            return ans

        return f(s)
