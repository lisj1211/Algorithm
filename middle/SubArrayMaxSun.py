# -*- coding: utf-8 -*-
# 为了保证招聘信息的质量问题，公司为每个职位设计了打分系统，打分可以为正数，也可以为负数，正数表示用户认可帖子质量，
# 负数表示用户不认可帖子质量．打分的分数根据评价用户的等级大小不定，比如可以为 -1分，10分，30分，-10分等。假设数组A
# 记录了一条帖子所有打分记录，现在需要找出帖子曾经得到过最高的分数是多少，用于后续根据最高分数来确认需要对发帖用户做
# 相应的惩罚或奖励．其中，最高分的定义为：用户所有打分记录中，连续打分数据之和的最大值即认为是帖子曾经获得的最高分。
# 例如：帖子10001010近期的打分记录为[1,1,-1,-10,11,4,-6,9,20,-10,-2],那该条帖子曾经到达过的最高分数为11+4+(-6)+9+20=38。
# 请实现一段代码，输入为帖子近期的打分记录，输出为当前帖子得到的最高分数。
from typing import List


def max_sum(arr: List[int]) -> int:
    max_ = float('-inf')
    cur = 0
    for num in arr:
        cur += num
        max_ = max(max_, cur)
        if cur < 0:
            cur = 0

    return max_


def max_sum1(arr: List[int]) -> int:
    max_ = float('-inf')
    pre = 0  # pre表示当前位置之前的累加和
    for num in arr:
        if pre < 0:  # 如果pre<0，表示负贡献
            pre = num
        else:
            pre += num
        max_ = max(max_, pre)

    return max_


if __name__ == '__main__':
    arr = [1, 1, -1, -10, 11, 4, -6, 9, 20, -10, -2]
    print(max_sum(arr))
    print(max_sum1(arr))
