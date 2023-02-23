# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        start = 0
        dic = {}
        for idx, ch in enumerate(s):
            if ch in dic:
                # start = max(start, dic[ch] + 1)
                start = start if start > dic[ch] + 1 else dic[ch] + 1  # 取两个数的最大值用if else比max快
            if idx - start + 1 > ans:
                ans = idx - start + 1

            dic[ch] = idx

        return ans


class Solution1:
    """暴力解"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans = 0
        length = len(s)
        for start in range(length):
            for end in range(1, length + 1):
                sub_len = len(s[start:end])
                if len(set(s[start:end])) == sub_len:
                    if sub_len > ans:
                        ans = sub_len

        return ans


class Solution2:
    """滑动窗口"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window = collections.deque()  # 无重复元素的子串窗口
        ans = 0
        start = 0
        for idx, ch in enumerate(s):
            if ch in window:  # 窗口内存在重复元素，则一直弹出
                while window.popleft() != ch:
                    start += 1
                start += 1
            if idx - start + 1 > ans:
                ans = idx - start + 1
            window.append(ch)

        return ans
