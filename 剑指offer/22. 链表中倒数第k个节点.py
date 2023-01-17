# -*- coding: utf-8 -*-
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
#
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    node = head
    for i in range(k):
        node = node.next
        if not node:
            if i == k - 1:  # 防止出现k等于链表长度的情况
                return head
            else:
                return None
    while node:
        head = head.next
        node = node.next
    return head


def getKthFromEnd1(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    cur = head
    for i in range(k):
        if not cur:  # 省一步判断操作
            return None
        cur = cur.next
    while cur:
        cur = cur.next
        head = head.next
    return head


if __name__ == '__main__':
    pass
