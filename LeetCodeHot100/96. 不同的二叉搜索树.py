# -*- coding: utf-8 -*-
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/unique-binary-search-trees/

class Solution:
    """
    假设 n 个节点存在二叉排序树的个数是 G (n)，令 f(i) 为以 i 为根的二叉搜索树的个数，则
    G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
    当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则
    f(i) = G(i-1)*G(n-i)

    """
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for num in range(2, n + 1):
            for l in range(num):
                r = num - l - 1
                dp[num] += dp[l] * dp[r]

        return dp[-1]
