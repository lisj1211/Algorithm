# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
# 分别完成在队列尾部插入整数和在队列头部删除整数的功能。
# (若队列中没有元素，deleteHead操作返回 -1 )
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
#
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
from collections import deque


class CQueue:

    def __init__(self):
        # 添加元素均进入stack1
        # stack2作用为弹出元素
        self.stack1 = deque()
        self.stack2 = deque()

    def append_tail(self, value: int) -> None:
        self.stack1.append(value)

    def delete_head(self) -> int:
        if self.stack2:
            return self.stack2.pop()

        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

        return -1
