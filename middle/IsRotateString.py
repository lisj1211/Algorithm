# -*- coding: utf-8 -*-
# 如果一个字符串为str，把字符串str前面任意的部分挪到后面形成的字符串叫作str的旋转词。比如str="12345"，str的旋转词有"12345"、"23451"、
# "34512"、"45123"和"51234"。给定两个字符串a和b，请判断a和b是否互为旋转词。
# 比如：
# a="cdab"，b="abcd"，返回true。
# a="1ab2"，b="ab12"，返回false。
# a="2ab1"，b="ab12"，返回true。


def is_rotate(str1, str2):  # 如果两字符串长度不一，直接false
    return len(str1) == len(str2) and str1 in str2 + str2
