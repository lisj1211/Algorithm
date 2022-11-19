# 给你一个字符串 s，找到 s 中最长的回文子串。
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/longest-palindromic-substring/description/
# 面试原题，没有一次性ac，中间判断子串首尾的index卡了一阵子，还得多多练习


def longest(s: str):
    string = "#" + "#".join(ch for ch in s) + "#"  # 插入#号便于忽略奇数和偶数长度
    length = 0
    res = ""
    for i in range(1, len(string) - 1):  # 忽略头尾的 #
        tmp = f(string, i)
        if tmp > length:
            length = tmp
            res = string[i - tmp + 1:i + tmp].replace("#", "")

    return res


def f(string, index):
    """
    返回以index位置为中心，向左右两边扩的最大长度
    :param string:
    :param index:
    :return:
    """
    res = 0
    l = r = index
    while l >= 0 and r < len(string):
        if string[l] == string[r]:
            res += 1
            l -= 1
            r += 1
        else:
            break

    return res


if __name__ == "__main__":
    print(longest("bwfabbafea"))
