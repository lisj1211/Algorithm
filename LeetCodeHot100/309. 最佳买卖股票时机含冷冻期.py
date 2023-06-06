# -*- coding: utf-8 -*-
# 给定一个整数数组prices，其中第prices[i]表示第i天的股票价格 。
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: prices = [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # s1表示当天不持股并且前一天也不持股
        # s2表示当天持股
        # s3表示当天不持股但前一天持股，即当天卖出
        s1, s2, s3 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            new_s1 = max(s1, s3)
            new_s2 = max(s2, s1 - prices[i])
            new_s3 = s2[1] + prices[i]
            s1, s2, s3 = new_s1, new_s2, new_s3

        return s1 if s1 > s3 else s3