# -*- coding: utf-8 -*-
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """归并"""
        m, n = len(nums1), len(nums2)
        ans = [0] * (m + n)
        i, j, idx = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans[idx] = nums1[i]
                i += 1
            else:
                ans[idx] = nums2[j]
                j += 1
            idx += 1
        ans[idx:] = nums1[i:] if i < m else nums2[j:]

        return ans[(m + n) // 2] if (m + n) & 1 != 0 else (ans[(m + n) // 2] + ans[(m + n) // 2 - 1]) / 2
