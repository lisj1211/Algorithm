# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
from collections import deque
from typing import List


# 单调队列
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        queue = deque()
        res = []
        # 保持单调队列头 -> 尾 依次递减
        for i in range(k):

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k, len(nums)):
            # 保持窗口大小，如果队头元素是要出队的元素，弹出
            if nums[i - k] == nums[queue[0]]:
                queue.popleft()
            # 队尾元素小于新的元素时，依次弹出队尾元素
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        ans = [queue[0]]
        for i in range(k, len(nums)):
            if nums[i - k] == queue[0]:
                queue.popleft()
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            ans.append(queue[0])
        return ans
