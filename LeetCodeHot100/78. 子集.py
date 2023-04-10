# -*- coding: utf-8 -*-
# 给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.f(nums, 0, [], ans)
        return ans

    def f(self, nums, idx, lst, res):
        if idx == len(nums):
            res.append(lst)
            return
        self.f(nums, idx + 1, lst, res)
        self.f(nums, idx + 1, lst + [nums[idx]], res)
