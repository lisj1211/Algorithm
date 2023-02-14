# 请实现两个函数，分别用来序列化和反序列化二叉树。

# 来源：力扣（LeetCode）
# https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 层序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        from collections import deque
        res = [str(root.val) + '_']
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                res.append(str(node.left.val) + '_')
            else:
                res.append('#_')

            if node.right:
                queue.append(node.right)
                res.append(str(node.right.val) + '_')
            else:
                res.append('#_')

        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        from collections import deque
        queue1 = deque(data.split('_')[:-1])
        root = TreeNode(int(queue1.popleft()))
        queue2 = deque([root])
        while queue2:
            node = queue2.popleft()
            left = queue1.popleft()
            right = queue1.popleft()
            if left != '#':
                node.left = TreeNode(int(left))
                queue2.append(node.left)
            if right != '#':
                node.right = TreeNode(int(right))
                queue2.append(node.right)

        return root


# 先序
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        def recur(node, lst):
            if not node:
                lst.append('#_')
                return
            lst.append(str(node.val) + '_')
            recur(node.left, lst)
            recur(node.right, lst)

        res = []
        recur(root, res)
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        from collections import deque
        queue = deque(data.split('_')[:-1])

        def recur(queue_):
            val = queue_.popleft()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = recur(queue_)
            root.right = recur(queue_)

            return root

        return recur(queue)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

