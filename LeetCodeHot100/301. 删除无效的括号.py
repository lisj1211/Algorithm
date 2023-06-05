# -*- coding: utf-8 -*-
# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。
#
# 返回所有可能的结果。答案可以按 任意顺序 返回。
#
# 示例 1：
#
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/remove-invalid-parentheses
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            l = 0
            for c in s:
                if c == '(':
                    l += 1
                elif c == ')':
                    if l <= 0:
                        return False
                    l -= 1

            return l == 0

        level = {s}
        while True:
            valid = [item for item in level if is_valid(item)]
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level
