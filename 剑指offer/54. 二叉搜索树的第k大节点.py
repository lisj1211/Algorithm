# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """中序遍历"""
    def kthLargest(self, root: TreeNode, k: int) -> int:
        lst = []
        self.mid_order(root, lst)
        return lst[-k]

    def mid_order(self, node, lst):
        if not node:
            return
        self.mid_order(node.left, lst)
        lst.append(node.val)
        self.mid_order(node.right, lst)


class Solution1:
    """先遍历右子树"""
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.f(root)
        return self.ans

    def f(self, node):
        if not node:
            return
        self.f(node.right)
        if self.k == 1:
            self.ans = node.val
        self.k -= 1
        self.f(node.left)


class Solution2:
    """提前返回"""
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.f(root)
        return self.ans

    def f(self, node):
        if not node:
            return
        self.f(node.right)
        if self.k == 0:  # 提前返回
            return
        if self.k == 1:
            self.ans = node.val
        self.k -= 1
        self.f(node.left)


