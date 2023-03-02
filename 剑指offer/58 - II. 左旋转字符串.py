# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
import collections


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        queue = collections.deque(s)
        queue.rotate(-n)
        return ''.join(list(queue))
