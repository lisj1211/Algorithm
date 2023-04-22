# -*- coding: utf-8 -*-
# 给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = float('inf')
        ans = 0
        for num in prices:
            if num - pre > ans:
                ans = num - pre
            if num < pre:
                pre = num

        return ans
