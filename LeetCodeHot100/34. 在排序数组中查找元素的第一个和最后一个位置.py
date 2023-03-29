# -*- coding: utf-8 -*-
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回[-1, -1]。
#
# 你必须设计并实现时间复杂度为O(log n)的算法解决此问题。
#
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = self.find_left(nums, target), self.find_right(nums, target)
        return [left, right] if left != -1 and right != -1 else [-1, -1]

    def find_left(self, nums, target):
        l, r = -1, len(nums)
        while l + 1 != r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return -1 if r == len(nums) or nums[r] != target else r

    def find_right(self, nums, target):
        l, r = -1, len(nums)
        while l + 1 != r:
            mid = l + ((r - l) >> 1)
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return -1 if l == -1 or nums[l] != target else l