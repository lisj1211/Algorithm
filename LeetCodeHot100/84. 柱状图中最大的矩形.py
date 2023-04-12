# -*- coding: utf-8 -*-
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode.cn/problems/largest-rectangle-in-histogram
from typing import List


class Solution:
    """简单直接想法，找到以每一位置为高的最大矩形面积，宽的左右边界分别为第一个比其小位置。结果超时"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 1:
            return heights[0]
        ans = 0
        for idx, h in enumerate(heights):
            l, r = idx - 1, idx + 1  # 左右边界
            while l >= 0:
                if heights[l] < h:  # 找到第一个比其小的左边界位置
                    break
                l -= 1

            while r < length:
                if heights[r] < h:  # 找到第一个比其小的右边界位置
                    break
                r += 1
            tmp = (r - l - 1) * h  # 计算此时面积
            if tmp > ans:
                ans = tmp  # 更新

        return ans


class Solution1:
    """优化找某一位置左右两边第一个小于其的数的位置"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 1:
            return heights[0]

        left = [-1] * length
        for i in range(1, length):
            if heights[i - 1] < heights[i]:  # 左边的数小于当前数
                left[i] = i - 1
            else:
                cur = left[i - 1] if i - 1 >= 0 else -1
                while cur >= 0 and heights[cur] >= heights[i]:  # cur往前窜，直到找到小于当前数的位置，思想类似最长公共子序列的next数组
                    cur = left[cur]
                left[i] = cur

        right = [length] * length
        for i in range(length - 2, -1, -1):
            if heights[i + 1] < heights[i]:
                right[i] = i + 1
            else:
                cur = right[i + 1] if i + 1 < length else length
                while cur <= length - 1 and heights[cur] >= heights[i]:
                    cur = right[cur]
                right[i] = cur

        ans = 0
        for idx, h in enumerate(heights):
            l, r = left[idx], right[idx]
            tmp = (r - l - 1) * h   # 计算此时面积
            if tmp > ans:
                ans = tmp  # 更新

        return ans


class Solution2:
    """用单调栈进一步优化"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        left, right = [0] * n, [0] * n

        mono_stack = []
        for i in range(n):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = []
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[i] <= heights[mono_stack[-1]]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return ans


class Solution3:
    """用单调栈进一步优化"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        ans = 0
        heights = [0] + heights + [0]  # 添加哨兵
        mono_stack = [0]
        for i in range(1, len(heights)):
            while mono_stack and heights[i] < heights[mono_stack[-1]]:
                h = heights[mono_stack.pop()]
                w = i - mono_stack[-1] - 1
                if w * h > ans:
                    ans = w * h
            mono_stack.append(i)

        return ans
