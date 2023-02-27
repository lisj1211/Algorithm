# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
# 输入: [7,5,6,4]
# 输出: 5


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.process(nums, 0, len(nums) - 1)

    def process(self, arr, left, right):
        if left == right:
            return 0
        mid = left + ((right - left) >> 1)
        ans = self.process(arr, left, mid) + self.process(arr, mid + 1, right)

        new_arr = [0] * (right - left + 1)
        idx = 0
        p, q = left, mid + 1
        while p <= mid and q <= right:
            if arr[p] > arr[q]:  # 结算左边比arr[p]大的，而不是右边比arr[q]小的
                new_arr[idx] = arr[q]
                # ans += q - mid  # 结算右边比arr[q]小的。这是错误的会漏掉一些
                ans += mid - p + 1  # 结算左边比arr[p]大的，正确的
                q += 1
            else:
                new_arr[idx] = arr[p]
                p += 1
            idx += 1
        new_arr[idx:] = arr[p:mid + 1] if q == right + 1 else arr[q:right + 1]
        arr[left:right + 1] = new_arr
        return ans