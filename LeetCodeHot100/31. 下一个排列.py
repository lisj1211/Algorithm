# -*- coding: utf-8 -*-
# 整数数组的一个 排列就是将其所有成员以序列或线性顺序排列。
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，
# 那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序
# 最小的排列（即，其元素按升序排列）。
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/next-permutation
from typing import List


class Solution:
    """
    从右往左找第一个降序的位置idx，如果都是升序，则说明现在已经是最大的组合，直接逆序即可
    在nums[idx+1:]从右往左找第一个大于nums[idx]的位置，交换后逆序右边部分即可，（核心：降序排列即为这一段数字的最大值）
    """
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        first_down = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_down = i
                break
        if first_down == -1:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, first_down, -1):
                if nums[i] > nums[first_down]:
                    nums[i], nums[first_down] = nums[first_down], nums[i]
                    self.reverse_list(nums, first_down + 1, len(nums) - 1)
                    break

    def reverse_list(self, lst, i, j):
        if i == j:
            return
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([2, 2, 0, 4, 3, 1]))
