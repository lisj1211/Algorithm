# 统计一个数字在排序数组中出现的次数。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        ans = 0
        for num in nums:
            if num == target:
                ans += 1
        return ans


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l = self.find_left(nums, target)
        r = self.find_right(nums, target)
        return r - l + 1 if 0 <= l < len(nums) and 0 <= r < len(nums) and nums[l] == target else 0

    def find_left(self, arr, target):
        l, r = -1, len(arr)
        while l + 1 != r:
            m = l + ((r - l) >> 1)
            if arr[m] < target:
                l = m
            else:
                r = m
        return r

    def find_right(self, arr, target):
        l, r = -1, len(arr)
        while l + 1 != r:
            m = l + ((r - l) >> 1)
            if arr[m] <= target:
                l = m
            else:
                r = m
        return l

