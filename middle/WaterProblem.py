# -*- coding: utf-8 -*-
# 给定一个数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水
# 比如，arr = {3，1，2，5，2，4}，根据值画出的直方图就是容器形状，该容器可以装下5格水,再比如，arr = {4，5，1，3，2}，该容器可以装下2格水


# i位置上方的水量为，i位置左侧的最大值和右侧的最大值的较小者减去i位置的值
def water_sum1(arr):
    if not arr or len(arr) < 3:
        return 0

    res = 0
    for i in range(1, len(arr) - 1):
        left_max = max(arr[:i])
        right_max = max(arr[i + 1:])
        res += max(min(left_max, right_max) - arr[i], 0)

    return res


def water_sum2(arr):
    if not arr or len(arr) < 3:
        return 0

    left_max = [-1] * len(arr)
    right_max = [-1] * len(arr)

    tmp = 0
    for i in range(1, len(arr)):
        left_max[i] = arr[i - 1] if arr[i - 1] > tmp else tmp
        tmp = left_max[i]
    tmp = 0

    for i in range(len(arr) - 2, 0, -1):
        right_max[i] = arr[i + 1] if arr[i + 1] > tmp else tmp
        tmp = right_max[i]

    res = 0
    for i in range(1, len(arr) - 1):
        res += max(min(left_max[i], right_max[i]) - arr[i], 0)

    return res


def water_sum3(arr):
    if not arr or len(arr) < 3:
        return 0

    left_max, right_max = arr[0], arr[-1]
    l, r = 1, len(arr) - 2  # 左右指针
    res = 0

    while l <= r:
        if left_max > right_max:  # r位置可以结算
            res += max(right_max - arr[r], 0)
            right_max = max(right_max, arr[r])
            r -= 1
        else:  # l位置可以结算
            res += max(left_max - arr[r], 0)
            left_max = max(left_max, arr[l])
            l += 1

    return res


if __name__ == '__main__':
    arr1 = [3, 1, 2, 5, 2, 4]
    print(water_sum1(arr1), water_sum2(arr1), water_sum3(arr1))
    arr2 = [4, 5, 1, 3, 2]
    print(water_sum1(arr2), water_sum2(arr2), water_sum3(arr2))
