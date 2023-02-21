# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，
# 第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
# 请写一个函数，求任意第n位对应的数字。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# 输入：n = 3
# 输出：3


class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1  # 当前i位数的起始数字
        digit = 1  # 当前是i位数
        count = 9  # 当前i位数总共有多少个数字
        while count < n:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit  # 9 * start * digit 计算i位数总共有多少个数字

        num = start + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])

