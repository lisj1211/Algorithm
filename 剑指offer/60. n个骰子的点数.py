# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
# 来源：力扣（LeetCode）
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
# 链接：https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/
from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1 / 6] * 6
        # 从第2个骰子开始，这里n表示n个骰子，先从第二个的情况算起，然后再逐步求3个、4个···n个的情况
        for i in range(2, n + 1):
            # i个骰子的取值范围即点数之和的值的个数是6*i-(i-1)，化简：5*i+1
            tmp = [0] * (5 * i + 1)
            # 第i-1个骰子，即上一个的结果为 dp,
            for j in range(len(dp)):
                # 上一轮的每个结果只会对其 +1 到 +6 的结果有影响
                # 比如只有1个骰子，dp[0]代表当骰子点数之和为1时的概率，它会对当有2个骰子时的点数之和2、3、4、5、6、7产生影响
                # 因为当有一个骰子的值为1时，另一个骰子的值可以为1~6，产生的点数之和相应的就是2~7
                # 所以k在这里就是对应着第i个骰子出现时可能出现六种情况
                for k in range(6):
                    # 这里记得是加上dp数组值与1/6的乘积，1/6是第i个骰子投出某个值的概率
                    tmp[j + k] += dp[j] / 6
            # 更新 dp 数组求下一轮
            dp = tmp
        return dp
