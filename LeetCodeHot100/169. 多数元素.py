# -*- coding: utf-8 -*-
# 给定一个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例1：
#
# 输入：nums = [3,2,3]
# 输出：3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/majority-element
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        ans = 0
        for num in nums:
            if ans == num:
                vote += 1
            else:
                if vote == 0:
                    ans = num
                    vote += 1
                else:
                    vote -= 1

        return ans
