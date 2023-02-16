# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值, 那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值, 那么中位数就是所有数值排序之后中间两个数的平均值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
import heapq


class MedianFinder:
    """
    分别建立一个大根堆和小根堆, 大根堆保存数组较小的部分, 小根堆保存较大的部分, 
    大根堆和小根堆的栈顶元素则是整个数据流的中位数
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []  # 大根堆
        self.small_heap = []  # 小根堆

    def addNum(self, num: int) -> None:
        min_num_in_small_heap = self.small_heap[0] if self.small_heap else float('-inf')
        if num > min_num_in_small_heap:  # 如果num大于小根堆栈顶, 则加入小根堆, 即较大的一部分
            heapq.heappush(self.small_heap, num)
            if len(self.small_heap) > len(self.big_heap) + 1:
                heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        else:
            heapq.heappush(self.big_heap, -num)
            if len(self.small_heap) > len(self.big_heap) + 1:
                heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))

    def findMedian(self) -> float:
        if self.big_heap or self.small_heap:
            if len(self.big_heap) == len(self.small_heap):
                return (-self.big_heap[0] + self.small_heap[0]) / 2
            return -self.big_heap[0] if len(self.big_heap) > len(self.small_heap) else self.small_heap[0]


class MedianFinder1:
    """
    第一种为先判断后加入元素, 当前方法设定如果为奇数时, 则大根堆元素比小根堆元素多一个.
    设定A为小根堆,B为大根堆;设A中有m个元素,B中有n个元素,
    1.当m=n时,num应该添加进B中,但num可能是较大的一半,因此先入堆A,再将A堆顶弹出入B
    2.当m=n+1时,num应该添加进A中,但num可能是较小的一半,因此先入堆B,再将A堆顶弹出入A
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []  # 大根堆
        self.small_heap = []  # 小根堆

    def addNum(self, num: int) -> None:
        if len(self.small_heap) == len(self.big_heap):
            heapq.heappush(self.small_heap, num)
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
            # heapq.heappush(self.big_heap, -heapq.heappushpop(self.small_heap, num)) 合为一步
        else:
            heapq.heappush(self.big_heap, -num)
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))
            # heapq.heappush(self.small_heap, -heapq.heappushpop(self.big_heap, -num)) 合为一步

    def findMedian(self) -> float:
        if self.big_heap or self.small_heap:
            return (self.small_heap[0] - self.big_heap[0]) / 2 if len(self.big_heap) == len(self.small_heap) else -self.big_heap[0]
