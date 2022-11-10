# -*- coding: utf-8 -*-
# arr表示每个咖啡机需要泡咖啡的时间，N表示有多少人需要喝咖啡，每个人只喝一杯。目前只有一台洗咖啡的机器，洗一杯的时间为a。b表示咖啡杯自然挥发变干
# 所需要的时间。问N个人从喝咖啡到所有咖啡杯洗完最少需要多少时间。
import heapq


def min_time(arr, n, a, b):
    heap = []  # heap元素为 (end_time, cur_time, work_time), 即(咖啡机下一次工作开始时间，当前时间点，咖啡机工作时间)
    for i in arr:
        heapq.heappush(heap, (i, 0, i))  # 按下一次的工作时间加入小根堆

    drink_time = []  # drink_time[i]表示某个人得到咖啡杯的时间，即该时刻产生一个需要清洗的杯子
    for i in range(n):
        end_time, cur_time, work_time = heapq.heappop(heap)
        drink_time.append(end_time)
        heapq.heappush(heap, (end_time + work_time, end_time, work_time))  # 更新时间点

    return f(drink_time, a, b, 0, 0)


def f(drinks, a, b, index, wash_line):
    """
    假设洗咖啡的机器在wash_line有空，洗完index之后的咖啡杯，返回最早完成的时间点
    :param drinks:
    :param a:
    :param b:
    :param index:
    :param wash_line:
    :return:
    """
    if index == len(drinks) - 1:
        return min(max(wash_line, drinks[index]) + a, drinks[index] + b)  # 洗咖啡杯和让它自然挥发的较小值，max表示必须等咖啡机空闲

    # 用咖啡杯洗
    wash = max(wash_line, drinks[index]) + a  # wash表示洗完当前咖啡杯的时间
    next1 = f(drinks, a, b, index + 1, wash)  # p1表示洗完剩下咖啡杯的时间
    p1 = max(wash, next1)  # 洗完当前咖啡杯，并且洗完剩下所有的咖啡杯，所以求最大值

    # 自然挥发
    dry = drinks[index] + b
    next2 = f(drinks, a, b, index + 1, wash_line)
    p2 = max(dry, next2)

    return min(p1, p2)


# def min_time_dp(arr, n, a, b):
#     heap = []
#     for i in arr:
#         heapq.heappush(heap, (i, 0, i))
#
#     drink_time = []
#     for i in range(n):
#         end_time, cur_time, work_time = heapq.heappop(heap)
#         drink_time.append(end_time)
#         heapq.heappush(heap, (end_time + work_time, end_time, work_time))
#
#     if a >= b:  # 如果洗一杯的时间大于自然挥发的时间，则全部自然挥发
#         return drink_time[-1] + b
#
#     dp = [[0 for _ in range(drink_time[-1] + n * a)] for _ in range(n)]
#     for i in range(drink_time[-1] + n * a):
#         dp[-1][i] = min(max(i, drink_time[-1]) + a, drink_time[-1] + b)
#     for row in range(n - 2, -1, -1):
#         for col in range(drink_time[-1] + n * a):
#             wash = max(col, drink_time[row]) + a
#             next1 = dp[row + 1][wash]
#             p1 = max(wash, next1)
#
#             dry = drink_time[row] + b
#             next2 = dp[row][col]
#             p2 = max(dry, next2)
#
#             dp[row][col] = min(p1, p2)
#
#     return dp[0][0]


if __name__ == '__main__':
    print(min_time([3, 2, 7], 10, 2, 5))


