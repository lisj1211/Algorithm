# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
# 示例:
#
# 输入: a = 1, b = 1
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof


class Solution:
    def add(self, a: int, b: int) -> int:
        a &= 0xffffffff  # 0xffffffff是为了控制在32位之内
        b &= 0xffffffff
        while b:
            a, b = a ^ b, (a & b) << 1 & 0xffffffff
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)
