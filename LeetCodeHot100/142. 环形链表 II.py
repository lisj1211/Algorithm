# -*- coding: utf-8 -*-
# 给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/linked-list-cycle-ii
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return None

        p1 = head.next
        p2 = head.next.next

        while p1 != p2:
            if not p2.next or not p2.next.next:
                return None
            p1 = p1.next
            p2 = p2.next.next

        p2 = head
        while p2 != p1:
            p1 = p1.next
            p2 = p2.next
        return p1
