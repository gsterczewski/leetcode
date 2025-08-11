# problem URL -> https://leetcode.com/problems/add-two-numbers
# difficulty: medium
# problem type: Linked List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # noinspection PyMethodMayBeStatic
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 1 if p1.val + p2.val > 9 else 0
        tail = ListNode((p1.val + p2.val) % 10)
        head = tail
        p1 = p1.next
        p2 = p2.next
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            tail.next = ListNode((v1 + v2 + carry) % 10)
            carry = 1 if v1 + v2 + carry > 9 else 0
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            tail = tail.next
        if carry > 0:
            tail.next = ListNode(carry)
        return head


def create_list_node(l):
    ln = ListNode(l[0])
    head = ln
    for i, item in enumerate(l):
        if i > 0:
            ln.next = ListNode(item)
            ln = ln.next
    return head


def print_list(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == '__main__':
    s = Solution()
    r1 = s.addTwoNumbers(create_list_node([2, 4, 3]), create_list_node([5, 6, 4]))
    r2 = s.addTwoNumbers(create_list_node([0]), create_list_node([0]))
    r3 = s.addTwoNumbers(create_list_node([9,9,9,9,9,9,9]), create_list_node([9,9,9,9]))
    print_list(r1)
    print("*"*30)
    print_list(r2)
    print("*"*30)
    print_list(r3)
