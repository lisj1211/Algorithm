# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof

# 输入: n = 5, m = 3
# 输出: 3


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# 笨办法
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if m == 1:
            return n - 1
        head = Node(0)
        cur = head
        for i in range(1, n):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head
        for _ in range(n - 1):
            for _ in range(m - 2):
                head = head.next
            head.next = head.next.next
            head = head.next

        return head.val


# 数组模拟
class Solution1:
    def lastRemaining(self, n: int, m: int) -> int:
        if m == 1:
            return n - 1
        lst = [i for i in range(n)]
        idx = 0
        for _ in range(n - 1):
            idx += m - 1
            idx %= len(lst)
            lst.remove(lst[idx])
        return lst[0]
