# -*- coding: utf-8 -*-
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    if not head:
        return head
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


def reverseList1(head: ListNode) -> ListNode:
    if not head:
        return head

    return recur(head)


def recur(node: ListNode):
    if not node.next:
        return node

    head = recur(node.next)
    node.next.next = node
    node.next = None

    return head


if __name__ == '__main__':
    pass
