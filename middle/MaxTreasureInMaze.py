# -*- coding: utf-8 -*-
# 来自美团
# 某天小美进入了一个迷宫探险，根据地图所示，这个迷宫里有无数个房间，序号分别为1，2，···入口房间的序号为1，
# 任意序号为正整数x的房间，都与序号 2*x 和2*x+1 的房间之间各有一条路径，但是这些路径都是单向的，即只能从序号x的房间
# 去序号为 2*x 和2*x+1 的房间而不能反向走，在任何时刻小美都可以选择结束探险并离开迷宫，但是离开之后无法在进入，
# 已知宝藏共有n个，其中第i个宝藏在序号为pi的房间，价值为wi，小美为了得到更多的宝藏，需要精心规划线路，问能获得的
# 宝藏价值和最大值为多少。
# 第一行为一个正整数n，表示宝藏数量
# 第二行为n个正整数，p1,```pn，其中pi表示第i个宝藏在序号为pi的房间
# 第三行为n个正整数，w1,```wn，其中wi表示第i个宝藏的价值为wi

from typing import List


def max_treasure(n: int, room_number: List[int], value: List[int]) -> int:
    """最大财宝数"""
    pairs = [(i, j) for i, j in zip(room_number, value)]
    pairs.sort()  # 按房间号排序
    num2val = dict(pairs)  # key:房间号, value:宝藏价值
    graph = {}  # key:房间号, value:下级路径房间号列表
    node_start = []  # 路径起始节点列表
    for num, val in pairs:  # 从小到大房间号遍历
        tmp = num
        while tmp:
            if tmp in graph:  # 如果tmp存在，在tmp后挂上num
                graph[tmp].append(num)
                break
            tmp //= 2  # 一直往上窜
        graph[num] = []
        if tmp == 0:  # tmp为0表示num为起始节点
            node_start.append(num)

    res = 0
    for start in node_start:  # 遍历所有起始节点，找到最大路径和
        res = max(res, recur(start, num2val, graph))

    return res


def recur(node, room_number_to_val, graph):
    """以node起始节点的最大路径和"""
    if not graph[node]:
        return room_number_to_val[node]

    max_ = 0
    for next in graph[node]:  # 找到最大的子路径和
        max_ = max(max_, recur(next, room_number_to_val, graph))

    return room_number_to_val[node] + max_


if __name__ == '__main__':
    print(max_treasure(15, [2, 3, 6, 7], [10, 1, 12, 8]))
