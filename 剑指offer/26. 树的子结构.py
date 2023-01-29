# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
# https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
#
# 输入：A = [1,2,3], B = [3,1]
# 输出：false


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if self.compare(A, B):
            return True
        if self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B):
            return True

        return False

    def compare(self, node1, node2):
        """比较以node1 和 node2为头结点的两棵树是否相同"""
        if not node2:
            return True
        if not node1 or node1.val != node2.val:
            return False

        return self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right)


# 精简
class Solution1:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        return self.compare(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def compare(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False

        return self.compare(A.left, B.left) and self.compare(A.right, B.right)
