# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
# 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof
import itertools
from typing import List


class Solution:
    def constructArr(self, a):
        if not a:
            return a
        length = len(a)
        ans = [1] * length
        tmp = 1
        for i in range(1, length):
            tmp *= a[i - 1]
            ans[i] *= tmp

        tmp = 1
        for i in range(length - 2, -1, -1):
            tmp *= a[i + 1]
            ans[i] *= tmp
        return ans


class Solution1:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return a
        left = [1] + list(itertools.accumulate(a, lambda x, y: x * y))[:-1]
        right = [1] + list(itertools.accumulate(reversed(a), lambda x, y: x * y))[:-1]
        right.reverse()
        ans = [1] * len(a)
        ans[0], ans[-1] = right[0], left[-1]
        for i in range(1, len(a) - 1):
            ans[i] = left[i] * right[i]
        return ans

