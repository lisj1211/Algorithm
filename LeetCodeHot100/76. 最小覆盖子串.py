# -*- coding: utf-8 -*-
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-window-substring
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):  # 如果原字符串长度小，直接返回
            return ''
        begin, max_len = 0, len(s) + 1  # max_len长度要大于len(s)，不然最后return判断会出错
        l = 0  # 左窗口索引
        need_dict = dict(collections.Counter(t))  # 每一个字符的要求数量
        need_count = len(t)  # 总共要求的字符数量
        for idx, ch in enumerate(s):  # idx表示右窗口索引
            if ch in need_dict:  # 如果右窗口字符在要求内
                need_dict[ch] -= 1    # 数量减1
                if need_dict[ch] >= 0:  # 只有当某个字符的要求数量大于等于0时，need_count减1，小于0时表示已冗余，保持need_count为0不变
                    need_count = need_count - 1

            while need_count == 0:  # 满足要求时更新
                if idx - l + 1 < max_len:
                    max_len = idx - l + 1
                    begin = l
                if s[l] in need_dict:  # 如果左窗口字符是要求字符
                    need_dict[s[l]] += 1
                    need_count = need_count + 1 if need_dict[s[l]] > 0 else 0  # 判断左窗口字符是否是冗余字符
                l += 1

        return s[begin: begin + max_len] if max_len <= len(s) else ""


s = Solution()
s.minWindow("a", "b")