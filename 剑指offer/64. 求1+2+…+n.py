# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/qiu-12n-lcof/

# 输入: n = 3
# 输出: 6


class Solution:
    def sumNums(self, n: int) -> int:
        return n and self.sumNums(n-1) + n
