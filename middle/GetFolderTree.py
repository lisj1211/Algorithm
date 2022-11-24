# -*- coding: utf-8 -*-
# 给你一个字符串类型的数组arr，譬如：arr = [ "b\\cst", "d\\", "a\\d\\e", "a\\b\\c" ];
# 你把这些路径中蕴含的目录结构给画出来，子目录直接列在父目录下面，并比父目录
# 向右进两格，就像这样:
# a
#   b
#     c
#   d
#     e
# b
#   cst
# d
# 同一级的需要按字母顺序排列，不能乱。
# 【思路】：前缀树加深度优先
from typing import List


class Node:
    def __init__(self, name):
        self.name = name
        self.next = {}


def print_directory(path_list: List[str]):
    root = generate_tree(path_list)
    print_tree(root, 0)


def generate_tree(path_list):
    """
    生成前缀树，每个节点表示一个目录节点
    :param path_list:
    :return:
    """
    root = Node('root')
    for path in path_list:
        cur = root
        lst = path.split('\\')
        if len(lst[-1]) == 0:  # 对于‘a\\’，splits之后会得到['a', '']，包含空串，之后打印时会多打出一个空格
            lst = lst[:-1]
        for tmp in lst:
            if tmp not in cur.next:
                cur.next[tmp] = Node(tmp)
            cur = cur.next[tmp]

    return root


def print_tree(node, level):
    if level == 1:
        print(node.name)
    if level > 1:
        print('  ' * (level - 1), node.name)

    for n in node.next.values():
        print_tree(n, level + 1)


if __name__ == '__main__':
    paths = ["b\\cst", "d\\", "a\\d\\e", "a\\b\\c"]
    print_directory(paths)
