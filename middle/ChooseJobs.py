# -*- coding: utf-8 -*-
# 为了找到自己满意的工作，牛牛收集了每种工作的难度和报酬。牛牛选工作的标准是在难度不超过自身能力
# 值的情况下，牛牛选择报酬最高的工作。在牛牛选定了自己的工作后，牛牛的小伙伴们来找牛牛帮忙选工作，
# 牛牛依然使用自己的标准来帮助小伙伴们。牛牛的小伙伴太多了，于是他只好把这个任务交给了你。
# 给定一个Job类型的数组jobarr，表示所有的工作。给定一个int类型的数组arr，表示所有小伙伴的能力。
# 返回int类型的数组，表示每一个小伙伴按照牛牛的标准选工作后所能获得的报酬。
from typing import List
from functools import cmp_to_key


class Job:
    def __init__(self, money, hard):
        self.money = money
        self.hard = hard


def get_money(jobs: List[Job], ability: List[int]) -> List[int]:
    job_list = [(job.hard, job.money) for job in jobs]
    job_list.sort(key=cmp_to_key(mycmp))  # 根据难度从小到大排序，难度相同的根据金钱从大到小排序
    aux = [job_list[0]]
    pre = job_list[0]
    for i in range(1, len(job_list)):  # 1. 对于难度相同的任务，只保留金钱最大的 2. 在难度变大的同时金钱也要变大
        if job_list[i][0] > pre[0] and job_list[i][1] > pre[1]:
            aux.append(job_list[i])
            pre = job_list[i]

    res = [search(aux, ab) for ab in ability]  # 二分查找小于等于能力的最大金钱

    return res


def mycmp(tuple1, tuple2):
    if tuple1[0] > tuple2[0]:
        return 1
    elif tuple1[0] < tuple2[0]:
        return -1
    else:
        if tuple1[1] < tuple2[1]:
            return 1
        elif tuple1[1] > tuple2[1]:
            return -1
        else:
            return 0


def search(arr, target):
    l, r = -1, len(arr)
    while l + 1 != r:
        mid = l + (r - l) // 2
        if arr[mid][0] <= target:
            l = mid
        else:
            r = mid

    return arr[l][1] if l != -1 else 0


if __name__ == '__main__':
    jobs = [Job(7, 5), Job(3, 12), Job(10, 12), Job(5, 13)]
    abilities = [2, 3, 5, 12, 15]
    print(get_money(jobs, abilities))
