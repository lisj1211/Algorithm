# -*- coding: utf-8 -*-
# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
# 要求：1.pop、push、getMin操作的时间复杂度都是O(1)；2.设计的栈类型可以使用现成的栈结构
from collections import deque


class Stack:
    def __init__(self):
        self.stack1 = deque()  # 操作栈
        self.stack2 = deque()  # 辅助栈

    def push(self, num):
        self.stack1.append(num)  # 操作栈正常压入
        if not self.stack2:  # 判断当前辅助栈的栈顶与num的大小，谁小压入谁
            self.stack2.append(num)
        elif self.stack2[-1] <= num:
            self.stack2.append(self.stack2[-1])
        else:
            self.stack2.append(num)

    def pop(self):
        if self.stack1:  # 共同弹出
            num = self.stack1.pop()
            self.stack2.pop()
            return num

        return None

    def get_min(self):
        return self.stack2[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    print(stack.get_min())
    stack.push(4)
    print(stack.get_min())
    stack.push(1)
    print(stack.get_min())
    print(stack.pop())
    print(stack.get_min())
