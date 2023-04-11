# -*- coding: utf-8 -*-
# 给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/word-search
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.f(board, word, i, j, 0, visited):
                    return True
        return False

    def f(self, board, word, i, j, idx, visited):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[idx]:
            return False

        visited[i][j] = True
        res = self.f(board, word, i - 1, j, idx + 1, visited) or self.f(board, word, i + 1, j, idx + 1, visited) \
              or self.f(board, word, i, j - 1, idx + 1, visited) or self.f(board, word, i, j + 1, idx + 1, visited)
        visited[i][j] = False
        return res
