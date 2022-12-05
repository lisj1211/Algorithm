# 给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true
# 否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
from typing import List


# primary
def exist(board: List[List[str]], word: str) -> bool:
    is_visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs1(board, row, col, word, 0, is_visited):
                return True

    return False


def dfs1(board, row, col, word, index, is_visited):
    if index == len(word):
        return True

    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or is_visited[row][col] or \
            board[row][col] != word[index]:
        return False

    is_visited[row][col] = 1
    res = dfs1(board, row + 1, col, word, index + 1, is_visited) or \
          dfs1(board, row, col + 1, word, index + 1, is_visited) or \
          dfs1(board, row - 1, col, word, index + 1, is_visited) or \
          dfs1(board, row, col - 1, word, index + 1, is_visited)
    is_visited[row][col] = 0
    return res


# 优化一：
def exist1(board: List[List[str]], word: str) -> bool:
    row, col = len(board), len(board[0])
    visited = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs2(board, row, col, i, j, visited, word, 0):
                return True

    return False


def dfs2(board, row, col, i, j, visited, word, k):
    if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] or word[k] != board[i][j]:
        return False
    if k == len(word) - 1:  # 第一个if过后 word[k] 已经与 board[i][j] 相等
        return True
    visited[i][j] = 1
    res = dfs2(board, row, col, i + 1, j, visited, word, k + 1) or \
        dfs2(board, row, col, i - 1, j, visited, word, k + 1) or \
        dfs2(board, row, col, i, j + 1, visited, word, k + 1) or \
        dfs2(board, row, col, i, j - 1, visited, word, k + 1)
    visited[i][j] = 0
    return res


# 优化二：visited用更改为空值做判断
def exist2(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, k):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[k] != board[i][j]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ' '  # 用空值替代
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = word[k]
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True

    return False
