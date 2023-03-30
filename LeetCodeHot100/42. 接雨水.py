# -*- coding: utf-8 -*-
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/trapping-rain-water
import itertools
from collections import namedtuple
from typing import List
import heapq


class Solution:
    """辅助数组"""
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        def f(x, y):
            return x if x > y else y

        left_max = [0] + list(itertools.accumulate(height, f))[:-1]  # 每一个位置其左边的最大值
        right_max = list(reversed(list(itertools.accumulate(reversed(height), f))))
        right_max = right_max[:-1] + [0]  # 每一个位置其右边的最大值

        ans = 0
        for i, num in enumerate(height):
            min_ = right_max[i] if left_max[i] > right_max[i] else left_max[i]  # 取二者较小的
            if min_ > num:
                ans += min_ - num  # 结算
        return ans


class Solution1:
    """最优解"""
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l_max, r_max = height[0], height[-1]  # 两边是不用结算的
        l, r = 1, len(height) - 2
        ans = 0
        while l <= r:
            # 当 l_max <= r_max 时，l位置左边的最大值确定为l_max，右边的最大值至少为r_max，因此可以更新l位置
            # 同理当 l_max > r_max 时，r位置右边的最大值确定为r_max，左边的最大值至少为l_max，因此可以更新r位置
            if l_max <= r_max:
                if l_max > height[l]:
                    ans += l_max - height[l]
                if l_max < height[l]:
                    l_max = height[l]
                l += 1
            else:
                if r_max > height[r]:
                    ans += r_max - height[r]
                if r_max < height[r]:
                    r_max = height[r]
                r -= 1
        return ans


# 拓展leetcode 407. 二维接雨水

class Solution3:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        Node = namedtuple('Node', ['value', 'x', 'y'])
        heap = []
        rows, cols = len(heightMap), len(heightMap[0])
        is_visited = [[0 for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]
        for col in range(cols - 1):
            heapq.heappush(heap, Node(heightMap[0][col], 0, col))
            is_visited[0][col] = 1
        for row in range(rows - 1):
            heapq.heappush(heap, Node(heightMap[row][cols - 1], row, cols - 1))
            is_visited[row][cols - 1] = 1
        for col in range(cols - 1, 0, -1):
            heapq.heappush(heap, Node(heightMap[rows - 1][col], rows - 1, col))
            is_visited[rows - 1][col] = 1
        for row in range(rows - 1, 0, -1):
            heapq.heappush(heap, Node(heightMap[row][0], row, 0))
            is_visited[row][0] = 1

        max_ = 0
        ans = 0
        while heap:
            val, x, y = heapq.heappop(heap)
            if val > max_:
                max_ = val
            if x > 0 and not is_visited[x - 1][y]:
                if heightMap[x - 1][y] < max_:
                    ans += max_ - heightMap[x - 1][y]
                heapq.heappush(heap, Node(heightMap[x - 1][y], x - 1, y))
                is_visited[x - 1][y] = 1
            if x < rows - 1 and not is_visited[x + 1][y]:
                if heightMap[x + 1][y] < max_:
                    ans += max_ - heightMap[x + 1][y]
                heapq.heappush(heap, Node(heightMap[x + 1][y], x + 1, y))
                is_visited[x + 1][y] = 1
            if y > 0 and not is_visited[x][y - 1]:
                if heightMap[x][y - 1] < max_:
                    ans += max_ - heightMap[x][y - 1]
                heapq.heappush(heap, Node(heightMap[x][y - 1], x, y - 1))
                is_visited[x][y - 1] = 1
            if y < cols - 1 and not is_visited[x][y + 1]:
                if heightMap[x][y + 1] < max_:
                    ans += max_ - heightMap[x][y + 1]
                heapq.heappush(heap, Node(heightMap[x][y + 1], x, y + 1))
                is_visited[x][y + 1] = 1
        return ans


if __name__ == '__main__':
    s = Solution3()
    print(s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))