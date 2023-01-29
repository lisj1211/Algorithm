# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_equal(root.left, root.right)

    def is_equal(self, node1, node2):
        """node1和node2为头结点的两棵树是否对称"""
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return self.is_equal(node1.left, node2.right) and self.is_equal(node1.right, node2.left)
        return False

