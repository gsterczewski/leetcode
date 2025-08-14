# PROBLEM URL -> https://leetcode.com/problems/linked-list-cycle


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm)/
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
s = Solution()
print(s.has_cycle(n1))
