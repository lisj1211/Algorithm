# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
# 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
from typing import List


# 方法一：排序
def find_repeat_number(nums: List[int]):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]

    return -1


# 方法二： 看见重复想到用 set()
def find_repeat_number1(nums: List[int]):
    myset = set()
    for num in nums:
        if num in myset:
            return num
        myset.add(num)

    return -1


# 方法三： 利用题目条件
def find_repeat_number3(nums: List[int]):
    for i in range(len(nums)):
        while i != nums[i]:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            # Python中， a, b = c, d操作的原理是先暂存元组(c,d) ，然后 “按左右顺序” 赋值给 a 和 b 。
            # 因此，若写为 nums[i], nums[nums[i]] = nums[nums[i]]
            # 则 nums[i]nums[i] 会先被赋值，之后 nums[nums[i]]nums[nums[i]] 指向的元素则会出错。

    return -1
