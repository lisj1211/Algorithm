# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
import math
from typing import List


class Solution:
    """双指针"""
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []
        sum_ = 3
        l, r = 1, 2
        end = (target + 1) // 2
        while r <= end:
            if sum_ == target:
                ans.append(list(range(l, r + 1)))
                sum_ -= l  # 找到之后要移动一步，不然会死循环
                l += 1
            elif sum_ > target:
                sum_ -= l
                l += 1
            else:
                r += 1
                sum_ += r
        return ans
