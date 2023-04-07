# -*- coding: utf-8 -*-
# 给定一个包含红色、白色和蓝色、共n 个元素的数组nums，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
#
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
#
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sort-colors
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        length = len(nums)
        l, r = -1, length
        i = 0
        while i < r:
            if nums[i] == 0:
                l += 1
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
