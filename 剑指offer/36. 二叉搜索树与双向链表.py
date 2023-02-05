# -*- coding: utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/?favorite=xb9nqhhg

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        from collections import deque
        queue = deque()
        self.recur(root, queue)
        ans = queue.popleft()
        pre = ans
        while queue:
            node = queue.popleft()
            pre.right = node
            node.left = pre
            pre = node

        ans.left = pre
        pre.right = ans

        return ans

    def recur(self, node, queue):
        if not node:
            return
        self.recur(node.left, queue)
        queue.append(node)
        self.recur(node.right, queue)


class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        head, tail = self.recur(root)
        head.left = tail
        tail.right = head
        return head

    def recur(self, node):
        if not node:
            return None, None
        left_head, left_tail = self.recur(node.left)
        right_head, right_tail = self.recur(node.right)

        if left_tail:
            node.left = left_tail
            left_tail.right = node
        if right_head:
            node.right = right_head
            right_head.left = node

        head = left_head if left_head else node
        tail = right_tail if right_tail else node

        return head, tail
