# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
# https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = set()
        for num in nums:
            if target - num in dic:
                return [num, target - num]
            dic.add(num)

        return []


class Solution1:
    """双指针"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ < target:
                l += 1
            elif sum_ > target:
                r -= 1
            else:
                return nums[l], nums[r]
