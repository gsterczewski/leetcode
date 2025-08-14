# PROBLEM URL -> https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# DIFFICULTY: Medium

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        target = head
        end = head
        # ustawiamy end w odległości n od target
        for _ in range(n-1):
            end = end.next
        # dojeżdżamy z end do końca listy
        while end.next:
            prev = target
            end = end.next
            target = target.next
        # teraz target wskazuje element do usunięcia
        # prev wskazuje element wcześniejszy

        # prev == head oznacza konieczność usunięcia pierwszego elementu listy
        if prev == target:
            head = head.next
            return head
        prev.next = target.next
        target.next = None
        return head

def print_list(head):
    while head:
        print(head.val)
        head = head.next

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
print("before remove n=2")
print_list(l1)

print("after remove n=2")
print_list(s.remove_nth_from_end(l1, 2))

l2 = ListNode(1)
l2.next = ListNode(2)
print("before remove n=1")
print_list(l2)

print("after remove n=1")
print_list(s.remove_nth_from_end(l2, 1))

l3 = ListNode(1)
print("before remove n=1")
print_list(l3)
print("after remove n=1")
print_list(s.remove_nth_from_end(l3, 1))

l1 = ListNode(1)
l1.next = ListNode(2)

print("before remove n=2")
print_list(l1)
print("after remove n=2")
print_list(s.remove_nth_from_end(l1, 2))