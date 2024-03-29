# -*- coding: utf-8 -*-
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
# 这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
#
# 示例：
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/implement-trie-prefix-tree


class TrieNode:
    def __init__(self):
        self.pass_by = 0
        self.end = 0
        self.next = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        self.root.pass_by += 1
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node.next[c].pass_by += 1
            node = node.next[c]
        node.end += 1

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]
        return node.end > 0

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.next:
                return False
            node = node.next[c]
        return True

    def delete(self, s: str):
        if self.search(s):
            node = self.root
            node.pass_by -= 1
            for ch in s:
                if node.nexts[ch].passby - 1 == 0:
                    del node.nexts[ch]
                    return
                node = node.nexts[ch]
                node.passby -= 1
            node.end -= 1

