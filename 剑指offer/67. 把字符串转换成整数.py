# 写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
# 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof

# 输入: "42"
# 输出: 42
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。


class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        int_max, int_min, int_boundary = 2**31 - 1, -2**31, 2**31//10
        res, idx, flag = 0, 1, 1
        if str[0] == '-':
            flag = -1
        elif str[0] != '+':
            idx = 0
        for char in str[idx:]:
            if char < '0' or char > '9':
                break
            if res > int_boundary or res == int_boundary and char > '7':
                return int_max if flag == 1 else int_min
            res = res*10 + ord(char) - ord('0')
        return flag*res



