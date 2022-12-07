# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
#
# 返回删除后的链表的头节点。
# https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
#
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(head: ListNode, val: int):
    if not head:
        return head
    if head.val == val:
        return head.next
    cur = head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
            break
        cur = cur.next

    return head


