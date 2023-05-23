# -*- coding: utf-8 -*-
# 给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。
# 滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sliding-window-maximum
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            if i < k:
                while queue and num > queue[-1]:
                    queue.pop()
                queue.append(num)
            else:
                ans.append(queue[0])
                while queue and num > queue[-1]:
                    queue.pop()
                queue.append(num)
                if queue[0] == nums[i - k]:
                    queue.popleft()
        ans.append(queue[0])

        return ans
