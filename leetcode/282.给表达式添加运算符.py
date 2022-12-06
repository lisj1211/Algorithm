# -*- coding: utf-8 -*-
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回所有能够
# 得到 target 的表达式。注意，返回表达式中的操作数 不应该 包含前导零。

# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"]
# 解释: “1*2*3” 和 “1+2+3” 的值都是6。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/expression-add-operators/description/
# 面试原题，直接懵逼，思路是递归，但是写不出来，下来自己看解答学习了一下
from typing import List


def addOperators(num: str, target: int) -> List[str]:
    res = []
    recur(num, '', 0, 0, target, 0, res)
    return res


def recur(num, tmp_str, index, sum_, target, mul, res):
    """
    :param num: 原始字符串
    :param tmp_str: 目前所构成的结果字符串
    :param index: 当前来到的index位置
    :param sum_: 目前所得到的结果
    :param target: 目标值
    :param mul: 前一个乘积
    :param res: 结果列表
    :return:
    """
    if index == len(num):  # 来到最后位置，判断结果是否相等
        if sum_ == target:
            res.append(tmp_str)
        return

    for i in range(index, len(num)):  # 两数之间可以不添加操作数，即可以多个进行结合
        if i > index and num[index] == '0':  # 不能有前导0
            break
        n = num[index:i + 1]  # 拿到范围值
        val = int(n)
        if index == 0:
            recur(num, tmp_str + n, i + 1, val, target, val, res)  # 是 i+1 而不是 index+1
        else:
            recur(num, tmp_str + '+' + n, i + 1, sum_ + val, target, val, res)
            recur(num, tmp_str + '-' + n, i + 1, sum_ - val, target, -val, res)
            recur(num, tmp_str + '*' + n, i + 1, sum_ - mul + val * mul, target, val * mul, res)