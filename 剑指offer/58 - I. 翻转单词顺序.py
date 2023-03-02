# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
# 例如输入字符串"I am a student. "，则输出"student. a am I"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof
# 输入: "the sky is blue"
# 输出: "blue is sky the"


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        s = [i for i in s if i]
        s.reverse()

        return " ".join(s)
