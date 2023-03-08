# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# 输入: [3,30,34,5,9]
# 输出: "3033459"
import functools
from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums) -> str:
        if len(nums) == 0:
            return str(0)

        def cmp(x1, x2):
            if str(x1) + str(x2) < str(x2) + str(x1):
                return -1
            elif str(x1) + str(x2) > str(x2) + str(x1):
                return 1
            else:
                return 0

        nums.sort(key=cmp_to_key(cmp))
        s = [str(i) for i in nums]
        return ''.join(s)


class Solution1:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            a = x + y
            b = y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(cmp))
        return ''.join(nums)
