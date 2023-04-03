# -*- coding: utf-8 -*-
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/maximum-subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')
        pre = 0  # 之前的子数组的最大和
        for num in nums:
            pre = num if pre < 0 else num + pre
            if pre > ans:
                ans = pre
        return ans
