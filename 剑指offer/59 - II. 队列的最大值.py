# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
# 若队列为空，pop_front 和 max_value需要返回 -1
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof

# 输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出:[null,null,null,2,1,2]
from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def max_value(self) -> int:
        return self.max_queue[0] if self.max_queue else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        num = self.queue.popleft()
        if num == self.max_queue[0]:
            self.max_queue.popleft()
        return num
