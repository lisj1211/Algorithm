# 输入一个字符串，打印出该字符串中字符的所有排列。

# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]


class Solution:
    def permutation(self, s: str) -> list[str]:
        s, res = list(s), []

        def dfs(k):
            if k == len(s):
                res.append(''.join(s))
            set1 = set()
            for i in range(k, len(s)):
                if s[i] in set1:
                    continue
                set1.add(s[i])
                s[k], s[i] = s[i], s[k]
                dfs(k+1)
                s[k], s[i] = s[i], s[k]
        dfs(0)
        return res


class Solution1:
    def permutation(self, s: str) -> list[str]:
        return list(set(''.join(i) for i in itertools.permutations(s, len(s))))

