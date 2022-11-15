# -*- coding: utf-8 -*-
# 在迷迷糊糊的大草原上，小红捡到了n根木棍，第i根木棍的长度为i，小红现在很开心。想选出其中的三根木棍组成美丽的三角形。
# 但是小明想捉弄小红，想去掉一些木棍，使得小红任意选三根木棍都不能组成三角形。请问小明最少去掉多少根木棍呢？
# 给定N，返回至少去掉多少根？

# 只保留斐波那契数列时，任意3根都无法组成三角形


def delete_num(n):
    if n < 4:
        return 0

    fib_num = 1
    a = b = 1
    while a <= n:
        a, b = b, a + b
        fib_num += 1

    return n - fib_num + 2


if __name__ == '__main__':
    print(delete_num(8))
