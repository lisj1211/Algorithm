# -*- coding: utf-8 -*-
# 如何仅用队列结构实现栈结构? 如何仅用栈结构实现队列结构?
from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()  # queue1为操作队列
        self.queue2 = deque()  # queue2为辅助队列

    def push(self, num):
        self.queue1.append(num)  # 只push queue1

    def pop(self):  # 先把queue1全部出队到queue2，只留下一个弹出元素，最后交换两个队列，保证queue1为操作队列
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop())
        num = self.queue1.pop()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return num


class Queue:
    def __init__(self):
        self.stack1 = deque()  # queue1为操作栈
        self.stack2 = deque()  # queue2为辅助栈

    def append(self, num):
        self.stack1.append(num)  # 只append queue1

    def poll(self):
        if not self.stack1 and not self.stack2:  # stack1,stack2都为空，返回none
            return None

        if not self.stack2:  # 如果stack2为空，则将stack1全部弹至stack2，最后返回stack2弹出元素
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
