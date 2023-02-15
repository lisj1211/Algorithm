# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
import heapq
from typing import List


class Solution:
    """排序"""
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k == 0:
            return []
        arr.sort()
        return arr[:k]


class Solution1:
    """库函数一步到位"""
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k == 0:
            return []
        return heapq.nsmallest(k, arr)


class Solution2:
    """手动实现大根堆"""
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k == 0:
            return []
        if len(arr) == k:
            return arr

        heap = []
        for i in range(k):
            heapq.heappush(heap, -arr[i])
        for i in range(k, len(arr)):
            heapq.heappushpop(heap, -arr[i])  # 可查看heappushpop说明

        return [-num for num in heap]
