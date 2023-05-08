# -*- coding: utf-8 -*-
# 给你两个单链表的头节点headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
#
# 图示两个链表在节点 c1 开始相交：
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/intersection-of-two-linked-lists


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length = 0
        cur = headA
        while cur:
            length += 1
            cur = cur.next
        cur = headB
        while cur:
            length -= 1
            cur = cur.next

        longer = headA if length > 0 else headB
        shorter = headB if longer == headA else headA

        if length < 0:
            length = -length
        for _ in range(length):
            longer = longer.next

        while longer and shorter:
            if shorter == longer:
                return shorter
            longer = longer.next
            shorter = shorter.next
        return None


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
