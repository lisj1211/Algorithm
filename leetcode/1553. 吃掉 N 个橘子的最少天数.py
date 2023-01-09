# -*- coding: utf-8 -*-
# 厨房里总共有 n个橘子，你决定每一天选择如下方式之一吃这些橘子：

# 吃掉一个橘子。
# 如果剩余橘子数n能被 2 整除，那么你可以吃掉 n/2 个橘子。
# 如果剩余橘子数n能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
# 每天你只能从以上 3 种方案中选择一种方案。
# 请你返回吃掉所有 n个橘子的最少天数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges

from typing import List


def min_days(n: int) -> int:
    mem = {}
    return mem_search(n, mem)


def mem_search(n: int, memory: dict):
    """记忆化搜索"""
    if n < 3:
        return n
    if n in memory:
        return memory[n]
    # 选择吃掉n/2，n%2为0，用一天吃掉一半橘子，n%2为1，先用一天吃一个橘子，在用一天吃掉一半橘子
    p1 = n % 2 + 1 + mem_search(n // 2, memory)
    # 选择吃掉2*(n/3)，n%3为0，用一天吃掉2*(n/3)橘子，
    # n%3为1，先用一天吃一个橘子，在用一天吃掉2*(n/3)橘子
    # n%3为2，先用两天吃两个橘子，在用一天吃掉2*(n/3)橘子
    p2 = n % 3 + 1 + mem_search(n // 3, memory)
    ans = min(p1, p2)
    memory[n] = ans

    return ans
