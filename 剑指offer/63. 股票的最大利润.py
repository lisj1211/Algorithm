# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof/
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        ans = 0
        pre = prices[0]  # 之前的最小值
        for i in range(1, len(prices)):
            tmp = prices[i] - pre  # 当天卖掉的利润
            if tmp > ans:
                ans = tmp  # 更新最大利润
            if prices[i] < pre:
                pre = prices[i]  # 更新最小值
        return ans
