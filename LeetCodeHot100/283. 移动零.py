# -*- coding: utf-8 -*-
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例 1:
#
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/move-zeroes
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        快排思想，将不为0的元素都往左移
        """
        left = -1
        for i, num in enumerate(nums):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]