# -*- coding: utf-8 -*-
# 给你一个整数数组nums，返回 数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积。
#
# 题目数据 保证 数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。
#
# 请不要使用除法，且在O(n) 时间复杂度内完成此题。
#
# 示例 1:
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/product-of-array-except-self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1  # ans[0]初始化为1，而不是nums[0]

        pre = 1
        for i in range(1, len(nums)):
            pre = pre * nums[i - 1]
            ans[i] = pre

        pre = 1
        for i in range(len(nums) - 2, -1, -1):
            pre = pre * nums[i + 1]
            ans[i] *= pre

        return ans
