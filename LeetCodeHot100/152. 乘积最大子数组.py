# -*- coding: utf-8 -*-
# 给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个32-位 整数。
#
# 子数组 是数组的连续子序列。
#
# 示例 1:
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释:子数组 [2,3] 有最大乘积 6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-product-subarray
from typing import List


class Solution:
    """因为有负数，所以除了最大值之外还要保存最小值"""
    def maxProduct(self, nums: List[int]) -> int:
        pre_max = 1
        pre_min = 1
        ans = float('-inf')
        for num in nums:
            # 分两行写会出错，因为第二行时pre_max已经更改，而pre_max和pre_min是需要同时更新的
            # pre_max = max(num, max(num * pre_max, num * pre_min))
            # pre_min = min(num, min(num * pre_max, num * pre_min))

            pre_max, pre_min = max(num, num * pre_max, num * pre_min), min(num, num * pre_max, num * pre_min)
            if pre_max > ans:
                ans = pre_max

        return ans