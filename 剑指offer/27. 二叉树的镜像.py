# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
# https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)

        root.left = right
        root.right = left

        return root


class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """自上而下交换左右节点"""
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root


class Solution2:
    """借助队列"""
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
