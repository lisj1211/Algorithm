# -*- coding: utf-8 -*-


def fib1(n):
    if n == 1 or n == 2:
        return 1

    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    a = b = 1
    while n - 1:
        a, b = b, a + b
        n -= 1

    return a


def fib3(n):
    """
    矩阵快速幂：对于任何当前状态只依赖前几个状态的问题均能用快速幂解决
    对于Fib(n) = Fib(n - 1) + Fib(n - 2) 只依赖前两个状态，即二阶问题
    [Fib(n)， Fib(n - 1)] = [Fib(n - 1)， Fib(n - 2)] * |a, b|
                                                       |c, d|

    [Fib(3)， Fib(2)] = [Fib(2)， Fib(1)] * |a, b|
                                           |c, d|
    a + c = 2
    b + d = 1

    [Fib(4)， Fib(3)] = [Fib(3)， Fib(2)] * |a, b|
                                           |c, d|
    2a + c = 3
    2b + d = 2

    a = 1, b = 1, c = 1, d = 0

    [Fib(n)， Fib(n - 1)] = [Fib(2)， Fib(1)] * |1, 1| (n - 2)次方
                                               |1, 0|

    因此问题为快速求[[1, 1], [1, 0]]的 n-2 次幂
    :param n:
    :return:
    """
    if n < 2:
        return 1
    base = [[1, 1], [1, 0]]
    res = matrix_power(base, n - 2)

    return res[0][0] + res[1][0]


def matrix_power(base, n):
    res = [[0 for _ in range(len(base))] for _ in range(len(base))]  # 矩阵中的1
    for i in range(len(base)):
        res[i][i] = 1

    while n:
        if n & 1 != 0:
            res = matrix_mul(res, base)
        base = matrix_mul(base, base)
        n >>= 1

    return res


def matrix_mul(matrix1, matrix2):
    res = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                res[i][j] += matrix1[i][k] * matrix2[k][j]

    return res


if __name__ == '__main__':
    print(fib1(5))
    print(fib2(5))
    print(fib3(5))


# 【拓展】
# 第一年有一只成年兔，成年兔每一年会生一只兔子，每只兔子需3年成熟，问n年后有多少兔子
# F(n) = F(n - 1) + F(n - 3)
# F(n - 1)表示去年的兔子， F(n - 3)表示3年前的兔子今年成年了

# 第一年有一只成年兔，成年兔每一年会生三只兔子，每只兔子需3年成熟，问n年后有多少兔子
# F(n) = F(n - 1) + 3 * F(n - 3)

# 第一年有一只成年兔，成年兔每一年会生三只兔子，每只兔子需3年成熟，每只兔子只能活5年，问n年后有多少兔子
# F(n) = F(n - 1) + 3 * F(n - 3) - F(n - 5)
