# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，
# 25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


# 动态规划：当前来到 i 位置，i位置的结果需要考虑 i-1 和 i-2 的结果
# f(i) = f(i-1) + f(i-2) 或 f(i) = f(i-1)
# f(i-2)当 i-1 和 i 拼起来小于26时成立，并且 i-1 > 0, 因为06不符合
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        str_num = list(str(num))
        a = 1
        b = 2 if str_num[0] + str_num[1] <= '25' else 1
        for i in range(2, len(str_num)):
            c = a + b if str_num[i-1] > '0' and str_num[i-1] + str_num[i] <= '25' else b
            a, b = b, c
        return b


class Solution1:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        str_num = list(str(num))

        return self.process(str_num, 0)

    def process(self, s: list, k: int):
        if k == len(s):
            return 1
        if s[k] == '1':
            res = 0
            res += self.process(s, k+1)
            if k + 1 < len(s):
                res += self.process(s, k+2)
            return res
        if s[k] == '2':
            res = 0
            res += self.process(s, k+1)
            if k + 1 < len(s) and '0' <= s[k+1] <= '5':
                res += self.process(s, k+2)
            return res

        return self.process(s, k+1)
