# -*- coding: utf-8 -*-
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/merge-k-sorted-lists
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """两两合并"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        list1 = lists[0]
        for i in range(1, len(lists)):
            list1 = self.merge_two_list(list1, lists[i])

        return list1

    def merge_two_list(self, list1, list2):
        if not list1 or not list2:
            return list1 if list1 else list2

        pre = ListNode()
        cur = pre

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return pre.next


class Solution1:
    """递归合并"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        list1 = lists[0]
        for i in range(1, len(lists)):
            list1 = self.merge_two_list(list1, lists[i])

        return list1

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + ((r - l) >> 2)
        left = self.merge(lists, l, mid)
        right = self.merge(lists, mid + 1, r)
        return self.merge_two_list(left, right)

    def merge_two_list(self, list1, list2):
        if not list1 or not list2:
            return list1 if list1 else list2

        pre = ListNode()
        cur = pre

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return pre.next


class Solution2:
    """辅助数组"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        nums = []
        for node in lists:
            while node:
                nums.append(node.val)
                node = node.next
        nums.sort()
        pre = ListNode()
        cur = pre
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return pre.next


class Solution3:
    """堆"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        pre = ListNode()
        cur = pre
        while heap:
            val, idx = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return pre.next


class Solution4:
    """堆"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def __lt__(self, other):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        pre = ListNode()
        cur = pre
        while heap:
            node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, node.next)

        return pre.next
