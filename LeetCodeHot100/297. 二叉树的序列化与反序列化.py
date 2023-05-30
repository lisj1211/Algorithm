# -*- coding: utf-8 -*-
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
# 同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
# 你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """先序"""
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def pre_order(node, s):
            if not node:
                ans.append("#")
                return
            ans.append(str(node.val))
            pre_order(node.left, s)
            pre_order(node.right, s)

        pre_order(root, ans)
        return '_'.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split('_'))

        def build(queue):
            ch = queue.popleft()
            if ch == '#':
                return None
            node = TreeNode(int(ch))
            node.left = build(queue)
            node.right = build(queue)

            return node

        return build(queue)


class Codec1:
    """层序"""
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"

        ans = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            val = str(node.val) if node else '#'
            ans.append(val)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return '_'.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return None

        queue1 = collections.deque(data.split('_'))
        root = TreeNode(int(queue1.popleft()))
        queue2 = collections.deque([root])

        while queue2:
            node = queue2.popleft()
            val = queue1.popleft()
            node.left = None if val == '#' else TreeNode(val)
            val = queue1.popleft()
            node.right = None if val == '#' else TreeNode(val)
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)

        return root

