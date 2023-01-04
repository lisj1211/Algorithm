# -*- coding: utf-8 -*-
# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。返回执行此操作后，grid 中最大的岛屿面积是多少？
# 示例 1:
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。

def largest_island(grid):
    res = 0
    land_name = 2
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                infect(grid, row, col, land_name)
                land_name += 1
    # 经过infect过程后，所有的小岛都变为相应的land_name
    if land_name == 2:  # grid全为0，将一格0变成1后返回1
        return 1

    land_size = [0] * land_name  # 相应数字的小岛对应的格子数
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                land_size[grid[row][col]] += 1  # 统计

    if land_size[-1] == len(grid) * len(grid[0]):  # grid全为1
        return land_size[-1]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                cur = get_size(grid, row, col, land_size)
                res = max(cur, res)

    return res


def infect(grid, i, j, island_name):
    """将grid[i][j]及其附近的1都变为 island_name"""
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return

    grid[i][j] = island_name
    infect(grid, i + 1, j, island_name)
    infect(grid, i - 1, j, island_name)
    infect(grid, i, j + 1, island_name)
    infect(grid, i, j - 1, island_name)


def get_size(grid, i, j, land_size):
    """获得grid[i][j]周围小岛总的数量"""
    visited = set()  # 过滤重复小岛
    visited.add(grid[i - 1][j] if i >= 1 else 0)
    visited.add(grid[i + 1][j] if i + 1 < len(grid) else 0)
    visited.add(grid[i][j - 1] if j >= 1 else 0)
    visited.add(grid[i][j + 1] if j + 1 < len(grid[0]) else 0)

    return sum(land_size[i] for i in visited) + 1


if __name__ == '__main__':
    # mat = [[1, 1, 1, 0, 0, 1, 1],
    #        [0, 1, 1, 0, 0, 0, 1],
    #        [0, 0, 0, 0, 0, 0, 0],
    #        [1, 1, 1, 0, 0, 0, 1],
    #        [1, 1, 1, 0, 1, 1, 1]]
    mat = [[0, 0],
           [0, 0]]
    print(largest_island(mat))
