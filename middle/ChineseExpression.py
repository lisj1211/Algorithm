# -*- coding: utf-8 -*-
# 把一个数字用中文表示出来。数字范围为 [0, 99999]。为了方便输出，使用字母替换相应的中文，万W 千Q 百B 十S 零L。
# 使用数字取代中文数字注：对于 11 应该表示为 一十一(1S1)，而不是十一(S1)
# 输入描述：
# 数字 0（包含）到 99999（包含）。
# 输出描述：
# 用字母替换相应的中文，万W 千Q 百B 十S 零L
# 示例1:
# 输入
# 12001
# 输出
# 1W2QL1


def convert(num: int) -> str:
    if num < 10:
        return str(num)

    num = str(num)
    length = len(num)
    bit = 'WQBSL'[5 - length:]  # 截取相应的单位列表
    res = [num[0] + bit[0]]  # 先直接获取最高位
    idx = 1
    pre = num[0]  # 记录前一位置信息
    while idx < length - 1:  # 从第二位开始遍历
        if num[idx] == '0':
            if pre != '0':  # 只有在第一次遇见0的时候补 L
                res.append('L')
        else:
            res.append(num[idx] + bit[idx])
        pre = num[idx]
        idx += 1

    if num[idx] == '0' and pre == '0':  # 如果最后一个和前一个都是0，则不需要 L
        res.pop()
    elif num[idx] != '0':
        res.append(num[idx])

    return ''.join(res)


if __name__ == '__main__':
    print(convert(12010))
