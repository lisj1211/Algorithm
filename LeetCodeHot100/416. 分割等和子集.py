# -*- coding: utf-8 -*-
# 给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 示例 1：
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/partition-equal-subset-sum
import functools
from typing import List


class Solution:
    """暴力递归"""
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ & 1 != 0:
            return False

        target = sum_ // 2

        def recur(i, cur):
            if cur > target or i == len(nums):
                return False

            if cur == target:
                return True

            return recur(i + 1, cur) or recur(i + 1, cur + nums[i])

        return recur(0, 0)


class Solution1:
    """记忆化搜索"""
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ & 1 != 0:
            return False

        target = sum_ // 2
        memory = {}

        def recur(i, cur):
            if cur > target or i == len(nums):
                return False

            key = str(i) + '_' + str(cur)
            if key in memory:
                return memory[key]

            if cur == target:
                return True

            ans = recur(i + 1, cur) or recur(i + 1, cur + nums[i])
            memory[key] = ans
            return ans

        return recur(0, 0)


class Solution2:
    """dp"""
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ & 1:
            return False

        target = sum_ // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]

            if dp[i][-1]:  # 提前判断
                return True

        return dp[-1][-1]