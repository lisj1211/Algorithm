# 编写一个函数，输入是一个无符号整数（以二进制串的形式），
# 返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
#
# 输入：n = 11 (控制台输入 00000000000000000000000000001011)
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011中，共有三位为 '1'。


def hammingWeight1(n: int) -> int:
    """
    最直接的方法
    """
    res = 0
    while n:
        if n & 1 == 1:
            res += 1
        n >>= 1
    return res


def hammingWeight2(n: int) -> int:
    res = 0
    while n:
        n &= n - 1  # 消除最右侧的1
        res += 1
    return res


def hammingWeight3(self, n: int) -> int:
    res = 0
    while n:
        leftone = n & (~n + 1)  # 取出最右侧的1
        n ^= leftone
        res += 1

    return res
