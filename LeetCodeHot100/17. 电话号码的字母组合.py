# -*- coding: utf-8 -*-
# 给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number
import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2str = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        lst = [num2str[ch] for ch in digits]
        ans = []
        for t in itertools.product(*lst):
            ans.append(''.join(t))
        return ans