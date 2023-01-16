# -*- coding: utf-8 -*-
# 来自hulu
# 有一个以原点为圆心，半径为1的圆。在这个圆的圆周上，有一些点，因为所有点都在圆周上，所以每个点可以通过弧度来表达。
# 比如：用0来表示一个圆周上的点，这个点就在(1，0)位置
# 比如：用6000来表示一个点，这个点是(1，0)点沿着逆时针转60.00度之后的位置
# 比如：用18034来表示一个点，这个点是(1，0)点沿着逆时针转180.34度之后的位置
# 这样以来，所有的点都可以用[0，36000)范围上的数字来表示
# 那么任意3个点都可以组成一个三角形，返回能组成三角形中构成钝角三角形的数量

from typing import List


def obtuse_triangle_num(points: List) -> int:
    """
    固定一个端点A，剩余两个端点在A+180度范围内任意选择，因为圆的直径与圆上任意一点都是直角三角形，
    遍历points列表，每个点都当作A端点，找到此时钝角三角形的数量，求和则为最终结果
    """
    points.sort()
    # 加36000为了方便计算以18000为A端点时的情况，添加数组避免其他处理
    enlarge = points + [p + 36000 for p in points]
    ans = 0
    left = 0
    for idx, degree in enumerate(points):
        while enlarge[left] < degree + 18000:
            left += 1
        degree_num = left - idx - 1
        # 至少得有2个点才能组成三角形
        ans += 0 if degree_num < 2 else degree_num * (degree_num - 1) // 2

    return ans


if __name__ == '__main__':
    print(obtuse_triangle_num([1000, 10000, 27000]))
