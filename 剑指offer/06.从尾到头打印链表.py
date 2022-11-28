# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
#
# 输入：head = [1,3,2]
# 输出：[2,3,1]
from collections import deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方法一：逆序先想到用栈
def reverse_print(head: ListNode):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    res = []
    while stack:
        res.append(stack.pop())

    return res


# 方法二：先遍历后逆序数组
def reverse_print1(head: ListNode):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    res.reverse()
    return res


# 方法三：从后往前放入数组
def reverse_print2(head: ListNode):
    if not head:
        return []
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    lst = [0] * count
    cur = head
    idx = 1
    while cur:
        lst[-idx] = cur.val
        idx += 1
        cur = cur.next

    return lst


# 方法四：反转链表
def reverse_print3(head: ListNode):
    if not head:
        return []
    lst = []
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next

    while pre:
        lst.append(pre.val)
        pre = pre.next

    return lst


# 方法五：反转链表-递归
def reverse_print4(head: ListNode):
    if not head:
        return []
    lst = []
    pre = reverse_list(head)
    while pre:
        lst.append(pre.val)
        pre = pre.next

    return lst


def reverse_list(head: ListNode):
    if not head or not head.next:
        return head
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None

    return p



