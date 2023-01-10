# -*- coding: utf-8 -*-
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# P(0)      A(4)      H(8)       N(12)
# A(1) P(3) L(5) S(7) I(9) I(11) G(13)
# Y(2)      I(6)      R(10)
# 输出："PAHNAPLSIIGYIR"

# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# P(0)           I(6)            N(12)
# A(1)      L(5) S(7)      I(11) G(13)
# Y(2) A(4)      H(8) R(10)
# P(3)           I(9)
# 输出："PINALSIGYAHRPI"

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zigzag-conversion


def convert(s: str, row: int) -> str:
    n = len(s)
    if row == 1 or n <= row:
        return s

    t = 2 * row - 2  # 两两竖行之间的差值
    ans = [''] * n
    idx = 0
    for i in range(row):  # 填写每一行
        j = i  # j为每一行的起始index
        while j < n:
            ans[idx] = s[j]
            idx += 1
            if j + t - 2 * i < n and 0 < i < row - 1:  # 中间行需要填写斜线部分
                ans[idx] = s[j + t - 2 * i]
                idx += 1
            j += t  # 下一个区间

    return ''.join(ans)


def convert1(s: str, row: int) -> str:
    if row == 1 or len(s) <= row:
        return s

    ans = [[] for _ in range(row)]  # 每一个元素代表每一行
    i, flag = 0, -1  # magic flag
    for char in s:
        ans[i].append(char)
        if i == 0 or i == row - 1:
            flag = -flag
        i += flag

    return ''.join(''.join(l) for l in ans)


if __name__ == '__main__':
    print(convert("PAYPALISHIRING", 4))
