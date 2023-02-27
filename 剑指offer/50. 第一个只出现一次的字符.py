# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
# 输入：s = "abaccdeff"
# 输出：'b'
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
        for ch in s:
            if dic[ch] == 1:
                return ch
        return " "


class Solution1:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return ' '
