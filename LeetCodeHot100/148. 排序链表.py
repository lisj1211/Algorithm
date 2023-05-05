# -*- coding: utf-8 -*-
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sort-list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst.sort()
        head = ListNode(0)
        cur = head
        for num in lst:
            cur.next = ListNode(num)
            cur = cur.next

        return head.next


class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 以下写法当有2个节点时会陷入死循环，while结束后，fast为none，slow为第二个节点
        # 之后mid为None，head依然为2个节点，无限递归
        # fast, slow = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        mid = slow.next
        slow.next = None

        left_head = self.sortList(head)
        right_head = self.sortList(mid)

        head = ListNode(0)
        cur = head
        while left_head and right_head:
            if left_head.val < right_head.val:
                cur.next = left_head
                left_head = left_head.next
            else:
                cur.next = right_head
                right_head = right_head.next
            cur = cur.next

        cur.next = left_head if left_head else right_head

        return head.next
