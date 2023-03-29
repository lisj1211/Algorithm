# -*- coding: utf-8 -*-
# 给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合，
# 并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为target 的不同组合数少于 150 个。
#
# 示例1：
#
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/combination-sum
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def f(nums, rest, idx, tmp):
            if rest == 0:
                ans.append(tmp)
                return
            if idx == len(nums):
                return
            for i in range(rest // nums[idx] + 1):  # 当前数添加若干次
                f(nums, rest - nums[idx] * i, idx + 1, tmp + [nums[idx]] * i)

        f(candidates, target, 0, [])
        return ans


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def f(nums, rest, idx, tmp):
            if rest == 0:
                ans.append(tmp)
                return
            if idx == len(nums):
                return
            if rest < nums[idx]:  # 如果当前数大于rest则不可能组成
                return
            for i in range(rest // nums[idx] + 1):
                f(nums, rest - nums[idx] * i, idx + 1, tmp + [nums[idx]] * i)

        candidates.sort()  # 排序进行加速
        f(candidates, target, 0, [])
        return ans


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2, 3, 6, 7], 7)
