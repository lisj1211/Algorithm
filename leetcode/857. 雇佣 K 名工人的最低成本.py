# -*- coding: utf-8 -*-
# 有n名工人。给定两个数组quality和zage，其中，quality[i]表示第i名工人的工作质量，其最低期望工资为wage[i]。
# 现在我们想雇佣k名工人组成一个工资组。在雇佣一组 k名工人时，我们必须按照下述规则向他们支付工资：
# 对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。
# 工资组中的每名工人至少应当得到他们的最低期望工资。
# 给定整数 k ，返回 组成满足上述条件的付费群体所需的最小金额。在实际答案的10e-5以内的答案将被接受。
#
# 示例 1：
# 输入： quality = [10,20,5], wage = [70,50,30], k = 2
# 输出： 105.00000
# 解释： 我们向 0 号工人支付 70，向 2 号工人支付 35。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/minimum-cost-to-hire-k-workers

from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        import heapq
        employees = [Employee(quality[i], wage[i]) for i in range(len(quality))]
        employees.sort(key=lambda x: x.rubbish_degree)
        # 根据degree排序，以每一个degree为基准，找前面quality总和最小的k-1个人

        res = float('inf')
        sum_ = 0
        heap = []  # 大根堆
        for idx, employee in enumerate(employees):
            if idx < k:  # 首先加入k个人
                sum_ += employee.quality
                heapq.heappush(heap, -employee.quality)
                if len(heap) == k:
                    res = min(res, sum_ * employee.rubbish_degree)
            else:  # 用当前的quality替换之前k个中最大的值
                sum_ += employee.quality + heapq.heappop(heap)
                heapq.heappush(heap, -employee.quality)
                res = min(res, sum_ * employee.rubbish_degree)

        return res


class Employee:
    def __init__(self, quality, wage):
        self.rubbish_degree = wage / quality  # 每一份能力所需要支付的薪水，k个人中已degree最大值为基准发薪资
        self.quality = quality


if __name__ == '__main__':
    s = Solution()
    print(s.mincostToHireWorkers([10, 20, 5], [70, 50, 30], 2))
