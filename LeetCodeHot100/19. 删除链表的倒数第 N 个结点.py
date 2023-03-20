# -*- coding: utf-8 -*-
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for _ in range(n):
            cur = cur.next
        if not cur:
            return head.next
        tmp = head
        while cur.next:
            tmp = tmp.next
            cur = cur.next
        tmp.next = tmp.next.next
        return head


class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0, head)
        p = q = pre

        for _ in range(n + 1):
            q = q.next

        while q:
            q = q.next
            p = p.next

        p.next = p.next.next

        return pre.next
