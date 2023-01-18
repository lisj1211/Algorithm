# -*- coding: utf-8 -*-
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 and not l2:
        return l1

    ans = ListNode(0)
    cur, node1, node2 = ans, l1, l2
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = ListNode(l1.val)
            l1 = l1.next
        else:
            cur.next = ListNode(l2.val)
            l2 = l2.next
        cur = cur.next

    cur.next = l1 if l1 else l2
    # while l1:
    #     cur.next = ListNode(l1.val)
    #     l1 = l1.next
    #     cur = cur.next

    # while l2:
    #     cur.next = ListNode(l2.val)
    #     l2 = l2.next
    #     cur = cur.next

    return ans.next


def mergeTwoLists1(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        ans = ListNode(0)
        cur = ans
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return ans.next
    else:
        return l1 if l1 else l2