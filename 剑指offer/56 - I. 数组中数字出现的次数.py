# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。# 链接：https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]


class Solution:
    def singleNumbers(self, nums):
        a = 0
        for num in nums:
            a ^= num
        right_one = a & (~a + 1)  # 取出最右侧的1
        b = 0
        for num in nums:
            if num & right_one == 0:
                b ^= num

        return [b, a ^ b]


    
