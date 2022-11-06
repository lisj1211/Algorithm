# -*- coding: utf-8 -*-
# 给定一个数组arr长度为N，你可以把任意长度大于0且小于N的前缀作为左部分，剩下的作为右部分。但是每种划分下都有左部分的最大值和右部分的最大值，
# 请返回最大的，左部分最大值减去右部分最大值的绝对值。


def max_abs1(arr):
    """
    先求左右两侧的最大值数组，之后直接从数组拿值
    :param arr:
    :return:
    """
    left_max, right_max = [arr[0]], [arr[-1]]
    tmp = arr[0]
    for i in range(1, len(arr)):  # 初始化左侧最大值数组
        left_max.append(max(tmp, arr[i]))
        tmp = left_max[i]
    tmp = arr[-1]
    for i in range(len(arr) - 2, -1, -1):    # 初始化右侧最大值数组
        right_max.insert(0, max(tmp, arr[i]))
        tmp = right_max[0]

    res = 0
    for i in range(0, len(arr) - 1):  # 左右两侧的最大值直接取
        res = max(res, abs(left_max[i] - right_max[i + 1]))

    return res


def max_abs2(arr):
    """
    题意即求 max(左) - max(右) 绝对值的最大值，而 max(左)，max(右)其一肯定是整个数组的最大值 max(arr)，
    若数组的最大值出现在左部分，则需要使得右侧部分的最大值最小，只有当右侧只有1个数时满足，return max(arr) - arr[-1]
    同理左侧部分，return max(arr) - arr[0]
    最终返回两者最大值
    :param arr:
    :return:
    """
    return max(arr) - min(arr[0], arr[-1])


if __name__ == '__main__':
    arr1 = [3, 1, 2, 5, 2, 4]
    print(max_abs1(arr1), max_abs2(arr1))
    arr2 = [4, 5, 1, 3, 2]
    print(max_abs1(arr2), max_abs2(arr2))

