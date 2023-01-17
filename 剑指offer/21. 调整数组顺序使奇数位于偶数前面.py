# -*- coding: utf-8 -*-
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
# https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?favorite=xb9nqhhg

from typing import List


def exchange(nums: List[int]) -> List[int]:
    if not nums:
        return nums
    even = len(nums)
    idx = 0
    while idx < even:
        if nums[idx] & 1 != 0:
            idx += 1
            continue
        else:
            even -= 1  # 移动偶数到右边
            nums[idx], nums[even] = nums[even], nums[idx]
    return nums


def exchange1(nums: List[int]) -> List[int]:
    if not nums or len(nums) == 1:
        return nums
    l, r = 0, len(nums) - 1
    while(l < r):
        while l < r and (nums[l] & 1) == 1:  # 从左往右找偶数
            l += 1
        while l < r and (nums[r] & 1) == 0:  # 从右往左找奇数
            r -= 1
        nums[l], nums[r] = nums[r], nums[l]  # 交换
    return nums


if __name__ == '__main__':
    print(exchange([1, 2, 3, 4]))
