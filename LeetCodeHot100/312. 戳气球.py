# -*- coding: utf-8 -*-
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组nums中。
#
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
# 这里的 i - 1 和 i + 1 代表和i相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
#
# 求所能获得硬币的最大数量。
#
# 示例 1：
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/burst-balloons
# 解析：https://leetcode.cn/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)

        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

        def score(i, j):
            max_ = 0
            for k in range(i + 1, j):
                tmp = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                if tmp > max_:
                    max_ = tmp

            dp[i][j] = max_

        for n in range(2, len(nums)):
            for start in range(len(nums) - n):
                score(start, start + n)

        return dp[0][-1]
