# PROBLEM URL -> https://leetcode.com/problems/partition-list
# DIFFICULTY: Medium
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        less = None
        more = None
        less_head = None
        more_head = None
        current = head
        while current:
            if current.val < x:
                if not less:
                    less = current
                    less_head = current
                else:
                    less.next = current
                    less = less.next
            else:
                if not more:
                    more = current
                    more_head = current
                else:
                    more.next = current
                    more = more.next

            current = current.next
        if not less_head:
            return more_head
        if not more_head:
            return less_head

        less.next = more_head
        more.next = None
        return less_head

