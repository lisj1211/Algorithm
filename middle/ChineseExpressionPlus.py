# -*- coding: utf-8 -*-
# 把一个数字用中文表示出来。
# 输入描述：
# 数字 -2 ** 31（包含）到 2 ** 31 - 1（包含）。
# 输出描述：
# 中文描述
# 示例1:
# 输入
# 1124263345
# 输出
# 十一亿两千四百二十六万三千三百四十五
# 示例2:
# 输入
# -720774515
# 输出
# 负七亿两千零七十七万四千五百一十五


def convert(num: int) -> str:
    if num == 0:
        return '零'

    res = '负' if num < 0 else ''
    num = -num if num < 0 else num
    yi = num // 100000000
    rest = num % 100000000
    if yi == 0:
        return res + num_1_to_99999999(rest)
    res += num_1_to_9999(yi) + '亿'
    if rest == 0:
        return res
    else:
        if rest < 10000000:
            return res + '零' + num_1_to_99999999(rest)
        else:
            return res + num_1_to_99999999(rest)


def num_1_to_9(num: int) -> str:
    if num < 1 or num > 9:
        return ''
    names = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
    return names[num - 1]


def num_1_to_99(num: int, has_bai: bool) -> str:
    if num < 1 or num > 99:
        return ''
    if num < 10:
        return num_1_to_9(num)
    shi = num // 10
    if shi == 1 and not has_bai:
        return '十' + num_1_to_9(num % 10)
    else:
        return num_1_to_9(shi) + '十' + num_1_to_9(num % 10)


def num_1_to_999(num: int) -> str:
    if num < 1 or num > 999:
        return ''
    if num < 100:
        return num_1_to_99(num, False)
    bai = num // 100
    res = num_1_to_9(bai) + '百'
    rest = num % 100
    if rest == 0:
        return res
    elif rest >= 10:
        return res + num_1_to_99(rest, True)
    else:
        return res + '零' + num_1_to_9(rest)


def num_1_to_9999(num: int) -> str:
    if num < 1 or num > 9999:
        return ''
    if num < 1000:
        return num_1_to_999(num)
    res = num_1_to_9(num // 1000) + '千'
    rest = num % 1000
    if rest == 0:
        return res
    elif rest >= 100:
        return res + num_1_to_999(rest)
    else:
        return res + '零' + num_1_to_99(rest, False)


def num_1_to_99999999(num: int) -> str:
    if num < 1 or num > 99999999:
        return ''
    wan = num // 10000
    rest = num % 10000
    if wan == 0:
        return num_1_to_9999(rest)
    res = num_1_to_9999(wan) + '万'
    if rest == 0:
        return res
    elif rest >= 1000:
        return res + num_1_to_9999(rest)
    else:
        return res + '零' + num_1_to_999(rest)


if __name__ == '__main__':
    print(convert(0))
    print(convert(2147483647))
    print(convert(-2147483648))
    print(convert(-2009956038))
    print(convert(-720774515))
    print(convert(-1626177776))
    print(convert(10))
    print(convert(110))
    print(convert(1010))
    print(convert(10010))