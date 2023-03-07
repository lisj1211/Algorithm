# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: TreeNode, o2: TreeNode) -> TreeNode:
        dic = {root: None}  # 节点到其父节点的映射
        self.f(root, dic)
        path = set()  # o1父节点的集合
        cur = o1
        while cur:
            path.add(cur)
            cur = dic[cur]
        cur = o2
        while cur:
            if cur in path:  # 出现在o1父节点集合中，则为共同节点
                return cur
            cur = dic[cur]

    def f(self, node, dic):
        if not node:
            return
        dic[node.left] = node
        dic[node.right] = node
        self.f(node.left, dic)
        self.f(node.right, dic)


class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p or root == q or root is None:  # 碰到p,q就返回
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left if left else right



