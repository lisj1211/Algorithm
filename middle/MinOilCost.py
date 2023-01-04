# -*- coding: utf-8 -*-
# 来自微软
# 给定2个数组A和B，如：
# A = [0, 1, 1]
# B = [1, 2, 3]
# A[0] = 0, B[0] = 1 表示0到1有双向道路
# A[0] = 1, B[0] = 2 表示1到2有双向道路
# A[0] = 1, B[0] = 3 表示1到3有双向道路
# 给定数字N，编号从0-N一共N+1个节点，保证一定都有所有节点并且没有环
# 默认办公室是0节点，其他1-N节点上，每个节点都有1个居民
# 每天所有居民都去0节点上班，所有居民都有一辆5座的车，也都乐意和别人一起乘车
# 车不管负重是多少，只要走过一条路，就耗费1的汽油，比如A,B,C的居民开自己的车来到D的位置，共耗费3的油
# D居民和E居民之间假设有一条道路，那么D可以接上A,B,C一起去E，只耗费1的油
# 求所有居民去办公室的路上，最少耗费多少汽油

from typing import List


def min_cost(list1: List[int], list2: List[int], n: int) -> int:
    """最少耗费多少油"""
    # 根据两个列表构建出图(邻接表法)
    size = [0] * n
    graph = [[] for _ in range(n)]
    for node1, node2 in zip(list1, list2):
        graph[node1].append(node2)
        graph[node2].append(node1)

    return dfs(0, -1, graph, size)


def dfs(cur_node: int, father_node: int, graph: List[List[int]], node_size: List[int]) -> int:
    """
    cur_node节点的所有子节点到cur_node需要花费多少油
    :param cur_node: 当前节点
    :param father_node: 当前节点的父节点
    :param graph: 图结构
    :param node_size: 每个节点包括自身有多少子节点
    :return:
    """
    total = 0
    node_size[cur_node] = 1  # 加上当前自身节点个数
    for child_node in graph[cur_node]:
        if child_node != father_node:  # father_node记录走过的路径
            cost = dfs(child_node, cur_node, graph, node_size)
            total += cost  # 加每个子节点的消耗
            total += (node_size[child_node] + 4) // 5  # 加每个子节点到当前节点的消耗，因为车可以坐5人，所以除以5向上取整
            node_size[cur_node] += node_size[child_node]

    return total


if __name__ == '__main__':
    A = [0, 1, 1]
    B = [1, 2, 3]
    print(min_cost(A, B, 4))
