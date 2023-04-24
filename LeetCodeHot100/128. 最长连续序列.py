# -*- coding: utf-8 -*-
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为O(n) 的算法解决此问题。
#
# 示例 1：
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-consecutive-sequence
from typing import List


# 题解：https://leetcode.cn/problems/longest-consecutive-sequence/solution/xiao-bai-lang-ha-xi-ji-he-ha-xi-biao-don-j5a2/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        ans = 0
        for num in set_:
            if num - 1 not in set_:
                cur = 1
                while num + 1 in set_:
                    cur += 1
                    num += 1
                if cur > ans:
                    ans = cur

        return ans


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        ans = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num - 1, 0)
                right = dic.get(num + 1, 0)
                cur = left + right + 1
                if cur > ans:
                    ans = cur

                dic[num] = cur
                dic[num - left] = cur
                dic[num + right] = cur

        return ans
