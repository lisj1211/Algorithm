# -*- coding: utf-8 -*-
# 给你一个整数 n ，对于0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：[0,1,1]
# 解释：
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/counting-bits
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(x):
            res = 0
            while x:
                if x & 1 == 1:
                    res += 1
                x >>= 1
            return res

        return [count_ones(x) for x in range(n + 1)]


class Solution1:
    def countBits(self, n: int) -> List[int]:
        def count_ones(x):
            res = 0
            while x:
                x &= x - 1  # 消除最右侧的1
                res += 1
            return res

        return [count_ones(x) for x in range(n + 1)]


class Solution2:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, len(ans)):
            if i & 1 == 1:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = ans[i // 2]

        return ans

