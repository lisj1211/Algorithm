# 输入两个链表，找出它们的第一个公共节点。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        cur = headA
        len_a = 0
        while cur:
            len_a += 1
            cur = cur.next
        cur = headB
        while cur:
            len_a -= 1
            cur = cur.next
        long_node = headA if len_a > 0 else headB
        short_node = headB if long_node is headA else headA
        cur = long_node
        if len_a < 0:
            len_a = -len_a
        for _ in range(len_a):
            cur = cur.next
        while cur:
            if cur == short_node:
                return cur
            cur = cur.next
            short_node = short_node.next

        return None


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
