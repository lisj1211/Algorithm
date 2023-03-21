# -*- coding: utf-8 -*-
# 数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/generate-parentheses
from typing import List


class Solution:
    """暴力求出所有的字符串，然后判断是否合法"""
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = []
        self.f(s, 2 * n, ans)
        return ans

    def f(self, s, length, lst):
        if length == 0:
            if self.check(s):
                lst.append(''.join(s))
            return
        s.append('(')
        self.f(s, length - 1, lst)
        s[-1] = ')'
        self.f(s, length - 1, lst)
        s.pop()

    def check(self, s):
        """判断合法性"""
        num = 0
        for ch in s:
            if ch == '(':
                num += 1
            else:
                num -= 1
                if num < 0:
                    return False
        return num == 0


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = []
        self.f(s, 2 * n, 0, ans)
        return ans

    def f(self, s, length, weight, lst):
        """
        :param s: 当前字符串
        :param length: 当前还剩下的长度
        :param weight: 合法性判断，左括号+1，右括号-1
        :param lst:
        :return:
        """
        if length == 0:
            if weight == 0:
                lst.append(''.join(s))
            return
        if weight < 0:
            return
        s.append('(')
        self.f(s, length - 1, weight + 1, lst)
        s[-1] = ')'
        self.f(s, length - 1, weight - 1, lst)
        s.pop()


class Solution2:
    """同Solution1，变化为用字符串而不是列表"""
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.f('', 2 * n, 0, ans)
        return ans

    def f(self, s, length, weight, lst):
        if length == 0:
            if weight == 0:
                lst.append(s)
            return
        if weight < 0:
            return
        s1 = s + '('
        self.f(s1, length - 1, weight + 1, lst)
        s2 = s + ')'
        self.f(s2, length - 1, weight - 1, lst)


class Solution3:
    """最优版，注：定义在函数内比定义在类内速度回快一点"""
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = ''

        def f(s, left, right):
            """
            :param s:
            :param left: 当前还有left个左括号可用
            :param right: 当前还有right个右括号可用
            :return:
            """
            if left == 0 and right == 0:
                ans.append(s)
                return
            if left > right:
                return
            if left > 0:
                f(s + '(', left - 1, right)
            if right > 0:
                f(s + ')', left, right - 1)

        f(s, n, n)
        return ans
