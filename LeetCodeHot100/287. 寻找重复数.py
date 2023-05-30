# -*- coding: utf-8 -*-
# 给定一个包含n + 1 个整数的数组nums ，其数字都在[1, n]范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
# 示例 1：
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-the-duplicate-number
from typing import List


class Solution:
    """参考找入环节点"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow
