# -*- coding: utf-8 -*-
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/reverse-linked-list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        while head:
            next_ = head.next
            head.next = pre
            pre = head
            head = next_

        return pre
