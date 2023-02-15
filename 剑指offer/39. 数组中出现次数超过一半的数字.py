# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
import collections
from typing import List


class Solution:
    """排序后返回中间元素"""
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


class Solution1:
    """用字典记录所有的次数"""
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        for num, count in dic.items():
            if count > len(nums)//2:
                return num


class Solution2:
    """摩尔投票"""
    def majorityElement(self, nums: List[int]) -> int:
        cur = 'num'
        sum_ = 0
        for num in nums:
            if num == cur:
                sum_ += 1
            else:
                if sum_ == 0:
                    cur = num
                    sum_ = 1
                else:
                    sum_ -= 1
        return cur
    