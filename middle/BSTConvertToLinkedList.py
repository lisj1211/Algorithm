# -*- coding: utf-8 -*-
# 双向链表节点结构和二叉树节点结构是一样的，如果你把last认为是left，next认为是next的话。
# 给定一个搜索二叉树的头节点head，请转化成一条有序的双向链表，并返回链表的头节点。
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def convert1(root: Node):
    queue = deque()
    inorder_to_list(root, queue)
    head = Node(queue.popleft())
    pre = head
    while queue:
        cur = Node(queue.popleft())
        pre.right = cur
        cur.left = pre
        pre = cur

    return head


def inorder_to_list(node: Node, queue: deque):
    if not node:
        return

    inorder_to_list(node.left, queue)
    queue.append(node.value)
    inorder_to_list(node.right, queue)


class Info:
    def __init__(self, node1, node2):
        self.headnode = node1
        self.tailnode = node2


def convert2(root: Node):

    return recur(root).headnode


def recur(node):
    if not node:
        return Info(None, None)

    left_info = recur(node.left)
    right_info = recur(node.right)

    if left_info.tailnode is not None:
        node.left = left_info.tailnode
        left_info.tailnode.right = node

    if right_info.headnode is not None:
        node.right = right_info.headnode
        right_info.headnode.left = node

    return Info(left_info.headnode if left_info.headnode is not None else node,
                right_info.tailnode if right_info.tailnode is not None else node)


if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(9)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.left.right.right = Node(4)
    head.right.left = Node(7)
    head.right.right = Node(10)
    head.left.left = Node(1)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)

    list_head = convert1(head)
    while list_head:
        print(list_head.value, end=' ')
        list_head = list_head.right

    print()
    list_head = convert2(head)
    while list_head:
        print(list_head.value, end=' ')
        list_head = list_head.right
