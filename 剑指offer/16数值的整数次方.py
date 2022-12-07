# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000


# 快速幂
def my_pow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n < 0:
        x = 1 / x
        n = -n

    res = 1
    base = x
    while n:
        if n & 1 != 0:
            res *= base

        base *= base
        n >>= 1

    return res
