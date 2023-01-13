# -*- coding: utf-8 -*-
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
#
# 数值（按顺序）可以分成以下几个部分：
# 1.若干空格
# 2.一个小数或者整数
# 3.（可选）一个'e'或'E'，后面跟着一个整数
# 4.若干空格

# 小数（按顺序）可以分成以下几个部分：
# 1.（可选）一个符号字符（'+' 或 '-'）
# 2.下述格式之一：
#   至少一位数字，后面跟着一个点 '.'
#   至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
#   一个点 '.' ，后面跟着至少一位数字
#
# 整数（按顺序）可以分成以下几个部分：
# 1.（可选）一个符号字符（'+' 或 '-'）
# 2.至少一位数字
#
# 部分数值列举如下：
# ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
# 部分非数值列举如下：
# ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof


def is_number(s: str) -> bool:
    s = s.strip()
    is_num = False
    has_e = False
    has_dot = False
    for idx, ch in enumerate(s):
        if '0' <= ch <= '9':
            is_num = True
        elif ch == '.':
            if has_dot or has_e:
                return False
            has_dot = True
        elif ch == 'e' or ch == 'E':
            if has_e or not is_num:
                return False
            has_e = True
            is_num = False
        elif ch == '-' or ch == '+':
            if idx != 0 and s[idx - 1] != 'e' and s[idx - 1] != 'E':
                return False
        else:
            return False

    return is_num


if __name__ == '__main__':
    print(is_number("aa"))
