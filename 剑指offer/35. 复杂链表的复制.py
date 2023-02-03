# -*- coding: utf-8 -*-
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_map = {}  # 原始节点 -> 复制节点映射
        cur = head
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:  # 根据原始节点找复制节点的next, random指针
            node_map[cur].next = node_map[cur.next] if cur.next else None
            node_map[cur].random = node_map[cur.random] if cur.random else None
            cur = cur.next

        return node_map[head]


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        1. 对每个节点建立复制节点: 1 -> 2 -> 3   ==>   1 -> 1 -> 2 -> 2 -> 3 -> 3
        2. 对每一对节点，根据前后关系链接random指针
        3. 分离复制节点
        """
        if not head:
            return None

        cur = head
        while cur:  # 第一步
            next = cur.next
            cur.next = Node(cur.val)
            cur.next.next = next
            cur = next

        cur = head
        while cur:  # 第二步
            copy_node = cur.next
            copy_node.random = cur.random.next if cur.random else None
            cur = copy_node.next

        cur = head
        ans = cur.next
        while cur:  # 第三步
            copy_node = cur.next
            cur.next = copy_node.next
            copy_node.next = copy_node.next.next if copy_node.next else None
            cur = cur.next

        return ans
