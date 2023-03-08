# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
# 请问该机器人能够到达多少个格子？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof

# 输入：m = 2, n = 3, k = 1
# 输出：3
import collections


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]
        return self.dfs(0, 0, m, n, k, visited)

    def dfs(self, i, j, m, n, k, visited):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or self.not_go(i, j, k):
            return 0
        visited[i][j] = True
        return 1 + self.dfs(i+1, j, m, n, k, visited) + self.dfs(i, j+1, m, n, k, visited)

    def not_go(self, i, j, k):
        res = 0
        while i:
            res += i%10
            i //= 10
        while j:
            res += j%10
            j //= 10
        return res > k


class Solution1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        queue = collections.deque()
        queue.append((0, 0))
        while queue:
            i, j = queue.popleft()
            if i < m and j < n and not visited[i][j] and not self.not_go(i, j, k):
                visited[i][j] = True
                res += 1
                queue.append((i+1,j))
                queue.append((i,j+1))
        return res

    def not_go(self, i, j, k):
        res = 0
        while i:
            res += i%10
            i //= 10
        while j:
            res += j%10
            j //= 10
        return res > k


class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        pass

