# -*- coding: utf-8 -*-
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/merge-intervals
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        j = 0
        i_l, i_r = intervals[0]
        while j < len(intervals):
            j_l, j_r = intervals[j]
            if j_l <= i_r:
                i_r = j_r if j_r > i_r else i_r
                j += 1
                continue
            else:
                ans.append([i_l, i_r])
                i_l, i_r = intervals[j]
        ans.append([i_l, i_r])
        return ans
