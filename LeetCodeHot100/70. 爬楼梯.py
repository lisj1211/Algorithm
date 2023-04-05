# -*- coding: utf-8 -*-
# 假设你正在爬楼梯。需要 n阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/climbing-stairs


class Solution:
    """递归"""
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1:
    """记忆化搜索"""
    def climbStairs(self, n: int) -> int:
        mem = [-1] * (n + 1)
        return self.f(n, mem)

    def f(self, n, memory):
        if n == 0 or n == 1:
            return 1
        if memory[n] != -1:
            return memory[n]
        memory[n] = self.f(n - 1, memory) + self.f(n - 2, memory)
        return memory[n]


class Solution2:
    """dp"""
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
