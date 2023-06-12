# -*- coding: utf-8 -*-
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/top-k-frequent-elements
import heapq
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [k for k, v in counter.most_common(k)]


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1

        dic = sorted(dic, key=lambda x: dic[x])
        return dic[-k:]


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        if k == len(counter):
            return list(counter.keys())

        heap = []
        for i, (num, count) in enumerate(counter.items()):
            if i < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

        return [c for n, c in heap]


s = Solution2()
s.topKFrequent([4,1,-1,2,-1,2,3], 2)
