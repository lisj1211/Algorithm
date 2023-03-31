# -*- coding: utf-8 -*-
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/permutations/?favorite=2cktkvj
import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def f(nums, idx):
            if idx == len(nums):
                ans.append(nums[:])
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                f(nums, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        f(nums, 0)
        return ans


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
