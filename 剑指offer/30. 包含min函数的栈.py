# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
# https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque
        self.stack = deque()
        self.min_stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            x = self.stack.pop()
            if x == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.min_stack[-1]

