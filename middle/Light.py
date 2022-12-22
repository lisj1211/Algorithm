# -*- coding: utf-8 -*-
# 小Q正在给一条长度为n的道路设计路灯安置方案。为了让问题更简单,小Q把道路视为n个方格,需要照亮的地方用'.'表示, 不需要
# 照亮的障碍物格子用'X'表示。小Q现在要在道路上设置一些路灯, 对于安置在pos位置的路灯, 这盏路灯可以照亮pos - 1, pos,
# pos + 1这三个位置。小Q希望能安置尽量少的路灯照亮所有'.'区域, 希望你能帮他计算一下最少需要多少盏路灯。


def min_light(s: str) -> int:
    if not s:
        return 0

    index, res = 0, 0
    while index < len(s):
        if s[index] == 'X':  # 当前位置是障碍物，跳过
            index += 1
        else:  # 当前位置是道路，给灯
            res += 1
            if index + 1 == len(s):  # 来到最后位置跳出循环
                break
            elif s[index + 1] == 'X':  # 下一个位置是障碍物，在当前位置给灯， index+2
                index += 2
            else:  # 下一个位置也是道路，在下个位置给灯， index+3,同时保证了当前位置之前的灯不会影响现在
                index += 3

    return res


if __name__ == '__main__':
    s = "...X.X.X..XX.XX.X.X.X.X.XX.XXX.X.XXX.XX"
    print(min_light(s))
