# PROBLEM URL -> https://leetcode.com/problems/middle-of-the-linked-list
# DIFFICULTY: Medium
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # naive approach
    def middleNodeNaive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodes = []
        length = 0
        temp = head
        while temp:
            nodes.append(temp)
            length += 1
            temp = temp.next
        return nodes[length // 2]
    # approach using 2 pointers: slow and fast
    def find_middle_node(self,head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
print(s.find_middle_node(l1).val)

