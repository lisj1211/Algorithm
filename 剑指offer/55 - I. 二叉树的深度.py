# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
# 输入: root = [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出: 3
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归"""
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1


class Solution1:
    """层序遍历"""
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        queue = collections.deque([root])
        while queue:
            ans += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
    
