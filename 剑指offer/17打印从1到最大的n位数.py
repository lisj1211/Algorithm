# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
#
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
from typing import List


def print_numbers(n: int) -> List[int]:
    return list(range(1, 10**n))
