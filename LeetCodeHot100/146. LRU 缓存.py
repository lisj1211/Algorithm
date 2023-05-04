# -*- coding: utf-8 -*-
# 请你设计并实现一个满足LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)如果关键字key 已经存在，则变更其数据值value ；如果不存在
# 则向缓存中插入该组key-value 。如果插入操作导致关键字数量超过capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/lru-cache


class Node:
    def __init__(self, key, val, next=None, pre=None):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:
    """双向链表 + 字典"""
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = self.head
        self.dict = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.delete_node(node)  # 将当前节点移至末尾
        self.add_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.delete_node(node)  # 将当前节点移至末尾
            self.add_node(node)
        else:
            if self.capacity == 0:  # 移除最不常用的节点
                delete_node = self.head.next
                self.dict.pop(delete_node.key)
                self.delete_node(delete_node)
                self.capacity += 1
            node = Node(key, value)
            self.add_node(node)
            self.capacity -= 1
            self.dict[key] = node

    def add_node(self, node):
        self.tail.next = node
        node.pre = self.tail
        self.tail = node

    def delete_node(self, node):  # 删除时考虑是否是尾节点
        if self.tail == node:
            self.tail = node.pre
            self.tail.next = None
            node.pre = Node
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = None
            node.next = None
