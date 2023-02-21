# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof

# 输入：n = 12
# 输出：5


class Solution:
    """
    例如求 2203 中所有1的个数，遍历每一分位，求当前位1的个数，最后相加。
    如当前来到十分位，即 22 [0] 3，记高位为high，低位为low，此时high为22，low为3
    1. 当前分位值为0
    2. 当前分位值为1
    3. 当前分位值为其他
    """

    def countDigitOne(self, n: int) -> int:
        n_str = str(n)
        str_len = len(n_str)
        idx = 0
        digit = 1
        ans = 0

        while idx < str_len:
            div, mod = divmod(n, digit)
            high = div // 10
            low = mod
            cur = int(n_str[str_len - idx - 1])
            if cur == 0:
                ans += high * digit
            elif cur == 1:
                ans += high * digit + low + 1
            else:
                ans += (high + 1) * digit
            digit *= 10
            idx += 1

        return ans


class Solution1:
    """简化版"""

    def countDigitOne(self, n: int) -> int:
        digit = 1
        ans = 0
        while digit <= n:
            high = n // (10 * digit)
            low = n % digit
            cur = (n // digit) % 10
            if cur == 0:
                ans += high * digit
            elif cur == 1:
                ans += high * digit + low + 1
            else:
                ans += (high + 1) * digit
            digit *= 10

        return ans
