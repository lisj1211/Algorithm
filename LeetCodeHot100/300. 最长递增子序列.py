# -*- coding: utf-8 -*-
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-increasing-subsequence
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > ans:
                ans = dp[i]

        return ans


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for i in range(len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            elif nums[i] < tail[-1]:
                l, r = -1, len(tail)
                while l + 1 != r:
                    m = (l + r) // 2
                    if tail[m] < nums[i]:
                        l = m
                    else:
                        r = m
                tail[r] = nums[i]

        return len(tail)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [0] * (len(nums) + 1)
        tail[0] = -float('inf')
        ans = 0
        for num in nums:
            if num > tail[ans]:
                ans += 1
                tail[ans] = num
            elif num < tail[ans]:
                l, r = 0, ans + 1
                while l + 1 != r:
                    m = (l + r) // 2
                    if tail[m] < num:
                        l = m
                    else:
                        r = m
                tail[r] = num
        return ans
