# -*- coding: utf-8 -*-
# 给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个下标。
#
# 示例1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/jump-game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        final = len(nums) - 1
        for idx, num in enumerate(nums):
            if idx > max_jump:
                return False
            if max_jump >= final:
                return True
            if idx + num > max_jump:
                max_jump = idx + num