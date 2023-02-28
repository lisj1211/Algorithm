# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/que-shi-de-shu-zi-lcof
# 输入: [0,1,3]
# 输出: 2
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx != num:
                return num
        return len(nums)


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = -1, len(nums)
        while l + 1 != r:
            mid = (l + r) // 2
            if mid == nums[mid]:
                l = mid
            else:
                r = mid
        return l + 1
