# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/chou-shu-lcof/
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n < 7:
            return n
        dp = [1]
        index_2 = index_3 = index_5 = 0
        for _ in range(1, n):
            mul2 = dp[index_2] * 2
            mul3 = dp[index_3] * 3
            mul5 = dp[index_5] * 5
            ans = min(mul2, mul3, mul5)
            dp.append(ans)
            if ans == mul2:
                index_2 += 1
            if ans == mul3:
                index_3 += 1
            if ans == mul5:
                index_5 += 1
        return dp[-1]


