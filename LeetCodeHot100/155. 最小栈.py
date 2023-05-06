# -*- coding: utf-8 -*-
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
#
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/min-stack
import collections


class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.aux = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.aux or val <= self.aux[-1]:  # 小于等于
            self.aux.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.aux[-1]:
            self.aux.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.aux:
            return self.aux[-1]


class MinStack1:
    """一个栈同时保存val和最小值"""
    def __init__(self):
        self.stack = collections.deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_ = val if val < self.stack[-1][1] else self.stack[-1][1]
            self.stack.append((val, min_))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
