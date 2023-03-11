# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，
# 而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof
# 输入: [1,2,3,4,5]
# 输出: True
# 输入: [0,0,1,2,5]
# 输出: True
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero_num = 0
        for i in range(4):
            if nums[i] == 0:
                zero_num += 1
                continue
            if nums[i] == nums[i + 1]:
                return False
        return nums[-1] - nums[zero_num] < 5


class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        set_ = set()
        min_, max_ = float('inf'), float('-inf')
        for num in nums:
            if num == 0:
                continue
            if num in set_:
                return False
            if num < min_:
                min_ = num
            if num > max_:
                max_ = num
            set_.add(num)
        return max_ - min_ < 5



