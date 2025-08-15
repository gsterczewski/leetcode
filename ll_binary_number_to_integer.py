# PROBLEM URL -> https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        sum = 0
        current = head
        while current:
            sum *= 2
            sum += current.val
            current = current.next
        return sum