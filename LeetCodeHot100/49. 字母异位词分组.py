# -*- coding: utf-8 -*-
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
#
# 示例 1:
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/group-anagrams
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]

        dic = collections.defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            dic[k].append(s)

        return [lst for lst in dic.values()]
