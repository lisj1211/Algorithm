# -*- coding: utf-8 -*-
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/valid-parentheses
import collections


class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0
