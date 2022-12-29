# -*- coding: utf-8 -*-
# 求完全二叉树的节点个数

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# 方法一：遍历
def node_num1(node: TreeNode) -> int:
    lst = []
    pre_order(node, lst)
    return len(lst)


def pre_order(node, order_list):
    """先序遍历"""
    if not node:
        return

    order_list.append(node.value)
    pre_order(node.left, order_list)
    pre_order(node.right, order_list)


# 方法二：
def node_num2(node: TreeNode) -> int:
    if not node:
        return 0

    return recur(node, 1, tree_depth(node, 1))


def tree_depth(node, level):
    """以node为根节点的完全二叉树的深度"""
    while node:
        level += 1
        node = node.left

    return level - 1


def recur(node, level, depth):
    """
    求以node为根节点的完全二叉树的节点个数
    :param node:
    :param level: 当前深度
    :param depth: 总深度
    :return:
    """
    if level == depth:  # 来到最后一层，即叶子节点，返回1
        return 1

    if tree_depth(node.right, level + 1) == depth:
        # 右树的深度为最大深度，说明左树为满二叉树，左树节点数 2**(depth-level)-1，加根节点1，加右树节点个数
        return 2 ** (depth - level) + recur(node.right, level + 1, depth)
    else:
        # 右树的深度非最大深度，说明右树为满二叉树，右树节点数 2**(depth-level-1)-1，加根节点1，加左树节点个数
        return 2 ** (depth - level - 1) + recur(node.left, level + 1, depth)


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    print(node_num1(head))
    print(node_num2(head))
