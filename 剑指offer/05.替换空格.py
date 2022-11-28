# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
#
# 输入：s = "We are happy."
# 输出："We%20are%20happy."


# 方法一：暴力寻找
def replace_space(s: str):
    return s.replace(" ", "%20")
