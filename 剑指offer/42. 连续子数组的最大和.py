# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
from typing import List


class Solution:
    """
    遍历求以每个元素为结尾的子数组的和，求最大值。
    1.当前元素为最后位置, pre + num
    2.只有当前元素, num
    """
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        pre = 0  # 之前的累加和
        for num in nums:
            pre = max(pre + num, num)
            ans = max(ans, pre)

            # 以下与上者等价，但是if else 比 max快近50%速度
            # pre = num if pre < 0 else pre + num
            # if pre > ans:
            #     ans = pre

        return ans