# 给定一个长度未N的数组，值一定在0 ~ N-1范围内，且每个值不重复，比如nums = [4, 2, 0, 3, 1]。把0想象为洞，任何非0的数字都
# 可以来到这个洞里，然后在原本的位置留下洞，比如4这个数字，来到0所代表的洞里，那么数组变为[0, 2, 4, 3, 1]，也就是原来的洞
# 被4填满，4走后留下了洞，任何数字只能搬家到洞里，并且走后留下洞，通过搬家的方式想变为有序的，有序有两种形式
# [0, 1, 2, 3, 4] 和 [1, 2, 3, 4, 0]
# 变为任意一种都可以，返回最少的搬动次数

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sort-numsay-by-moving-items-to-empty-space/

# 思路：
# 对于方案一，其index和index位置上的数是相等的，则按值找环，对于位置0，排序后应为0，则按index_4, index1, index_2, 找到0
# 此时的环有4个数，交换3次即可，对于没有0的环，因为题目要求必须每次跟0交换，则先随机将一个数跟0交换后重复过程即可

from typing import List
import random


def zuo(nums: List[int]) -> int:
    """按索引找"""
    n = len(nums)
    ans1 = 0
    ans2 = 0
    touched = [False] * n  # 标记已经交换过的，即最终位置是正确的
    for i in range(n):
        if not touched[i]:  # 如果当前位置没有动过，则进行找环过程
            m = 1
            touched[i] = True  # 标记
            next_ = nums[i]  # 下一位置的index
            while next_ != i:
                m += 1
                touched[next_] = True
                next_ = nums[next_]

            if m > 1:
                ans1 += m - 1 if i == 0 else m + 1

    # 方案二：变为[1, 2, 3, 4, 0]，对于0，其index为n-1，其他数的index为num-1
    touched = [False] * n
    for i in range(n - 1, -1, -1):
        if not touched[i]:
            m = 1
            touched[i] = True
            next_ = n - 1 if nums[i] == 0 else nums[i] - 1
            while next_ != i:
                m += 1
                touched[next_] = True
                next_ = n - 1 if nums[next_] == 0 else nums[next_] - 1

            if m > 1:
                ans2 += m - 1 if i == n - 1 else m + 1

    return min(ans1, ans2)


def min_move(nums: List[int]) -> int:
    """按值找，即index位置放得数是index，找值为index的数"""
    # 方案一：变为[0, 1, 2, 3, 4]
    ans1 = 0
    touched = [False] * len(nums)
    for i in range(len(nums)):
        # 如果i==nums[i]则已经是最终位置，
        # 如果nums[i] != i并且touched[i]表示之前已经交换过，同样可以略过
        if nums[i] != i and not touched[i]:  # 对于i位置而言，其位置上的最终结果应为i
            m = 1
            touched[i] = True
            next_idx = nums[i]  # 下一个位置索引
            while nums[next_idx] != i:  # 找到i
                m += 1
                touched[next_idx] = True
                next_idx = nums[next_idx]
            touched[next_idx] = True  # 这种方法需要考虑边界，当nums[next_idx] == i时，next_idx位置也要标记
            ans1 += m if i == 0 else m + 2

    # 方案二：变为[1, 2, 3, 4, 0]
    ans2 = 0
    touched = [False] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        true_num = 0 if i == len(nums) - 1 else i + 1  # 目标值
        if nums[i] != true_num and not touched[i]:
            m = 1
            touched[i] = True
            next_idx = len(nums) - 1 if nums[i] == 0 else nums[i] - 1
            while nums[next_idx] != true_num:
                m += 1
                touched[next_idx] = True
                next_idx = len(nums) - 1 if nums[next_idx] == 0 else nums[next_idx] - 1
            touched[next_idx] = True
            ans2 += m if i == len(nums) - 1 else m + 2

    return min(ans1, ans2)


if __name__ == '__main__':
    for _ in range(100):
        length = random.randint(4, 10)
        nums = list(range(length))
        random.shuffle(nums)
        if min_move(nums) != zuo(nums):
            print('fuck')
            break
    else:
        print('ok')
