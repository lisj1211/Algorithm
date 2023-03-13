# -*- coding: utf-8 -*-
# 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/add-two-numbers
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        flag = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            tmp = a + b + flag
            flag = 0
            if tmp > 9:
                flag = 1
                tmp %= 10
            cur.next = ListNode(tmp)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if flag:  # 最后还有可能多出一个1
            cur.next = ListNode(1)
        return ans.next