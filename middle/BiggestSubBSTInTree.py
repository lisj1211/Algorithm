# -*- coding: utf-8 -*-
# 找到一棵二叉树中，最大的搜索二叉子树，返回最大搜索二叉子树的节点个数。
# 拓展：返回最大搜索二叉子树的头结点


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Info:
    """
    二叉树递归套路，左右树返回信息
    """
    def __init__(self, max_val, min_val, num_nodes, is_BST, head):
        self.max_val = max_val
        self.min_val = min_val
        self.num_nodes = num_nodes
        self.is_BST = is_BST
        self.head = head


def biggest_node(head: Node):
    return recur(head)


def recur(node: Node):
    if not node:
        return Info(float('-inf'), float('inf'), 0, True, None)

    left_info = recur(node.left)
    right_info = recur(node.right)

    # 可能性一：最大二叉树的信息在左子树或右子树上
    max_ = max(left_info.max_val, right_info.max_val, node.value)
    min_ = max(left_info.min_val, right_info.min_val, node.value)
    max_nodes = max(left_info.num_nodes, right_info.num_nodes)
    max_head = left_info.head if max_nodes == left_info.num_nodes else right_info.head
    is_bst = False

    # 以node为头结点的整棵树都是BST
    if left_info.is_BST and right_info.is_BST and left_info.max_val < node.value < right_info.min_val:
        max_nodes = left_info.num_nodes + right_info.num_nodes + 1
        max_head = node
        is_bst = True

    return Info(max_, min_, max_nodes, is_bst, max_head)


if __name__ == '__main__':
    head = Node(6)
    head.left = Node(1)
    head.left.left = Node(0)
    head.left.right = Node(3)
    head.right = Node(12)
    head.right.left = Node(10)
    head.right.left.left = Node(4)
    head.right.left.left.left = Node(2)
    head.right.left.left.right = Node(5)
    head.right.left.right = Node(14)
    head.right.left.right.left = Node(11)
    head.right.left.right.right = Node(15)
    head.right.right = Node(13)
    head.right.right.left = Node(20)
    head.right.right.right = Node(16)
    print(biggest_node(head).head.value)
