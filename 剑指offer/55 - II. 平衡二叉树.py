# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/ping-heng-er-cha-shu-lcof/
# 输入: root = [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出: true


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.info(root)[0]

    def info(self, node):
        if not node:
            return True, 0
        l_info = self.info(node.left)
        r_info = self.info(node.right)
        height = max(l_info[1], r_info[1]) + 1
        is_bt = l_info[0] and r_info[0] and abs(l_info[1] - r_info[1]) < 2
        return is_bt, height

    
