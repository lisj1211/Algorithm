# -*- coding: utf-8 -*-
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
# 示例 1：
#
#
# 输入：head = [1,2,2,1]
# 输出：true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/palindrome-linked-list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        i, j = 0, len(lst) - 1

        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1

        return True


class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        n1 = n2 = head
        while n2.next and n2.next.next:
            n1 = n1.next
            n2 = n2.next.next

        n3 = n1.next
        n3 = self.reverse_list(n3)
        n4 = head
        while n4 and n3:
            if n4.val != n3.val:
                return False
            n4 = n4.next
            n3 = n3.next

        n1.next = self.reverse_list(n3)

        return True

    def reverse_list(self, node):
        pre = None
        while node:
            next_ = node.next
            node.next = pre
            pre = node
            node = next_

        return pre