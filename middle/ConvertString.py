# -*- coding: utf-8 -*-
# 给定一个字符串，如果该字符串符合人们日常书写一个整数的形式，返回int类型的这个数；如果不符合或者越界返回-1或者报错。
MAX = 2147483647
MIN = -2147483648


def convert_string(s: str) -> int:
    if not s:
        return -1

    if not is_valid(s):
        return -1

    res = 0
    chu = MIN / 10
    yu = MIN % 10

    flag = s[0] == '-'
    start = 1 if flag else 0
    for i in range(start, len(s)):
        cur = ord('0') - ord(s[i])  # 整体变为负数，因为负数绝对值比正数大1，如果按正数来转，则转换-2147483648时会出错

        if res < chu or (res == chu and cur < yu):  # 防止其他语言溢出
            return -1

        res = res * 10 + cur

    if not flag and res == MIN:  # 2147483648
        return -1

    return res if flag else -res


def is_valid(s):
    if s[0] != '-' and (s[0] < '0' or s[0] > '9'):  # 开头只能是 -号或者数字
        return False
    if s[0] == '-' and (len(s) == 1 or s[1] == '0'):  # 开头如果是-号，则后面必须有数并且不能为0
        return False
    if s[0] == '0' and len(s) > 1:  # 开头如果是0，则后面不能再有数字
        return False
    for i in range(1, len(s)):
        if s[i] < '0' or s[i] > '9':
            return False

    return True


if __name__ == '__main__':
    print(convert_string("-2147483648"))
