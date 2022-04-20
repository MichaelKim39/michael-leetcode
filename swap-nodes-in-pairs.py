"""
Question - https://leetcode.com/problems/swap-nodes-in-pairs/
Answer - https://leetcode.com/problems/swap-nodes-in-pairs/discuss/1163702/Python3-Simple-recursive-solution-beats-95.00-(easily-understandable-with-figure-explanation)

Two pointers
Progress by two at a time, until furthest is undefined
Swap at each node
"""

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        cur = head

        try:

            # locate head of next pair
            next_pair = cur.next.next

            # reverse next pair
            junction = self.swapPairs(next_pair)

            # reverse current pair
            original_next = cur.next

            original_next.next = cur

            # build new linkage from current pair to next pair
            cur.next = junction

            return original_next

        except:

            # Base case:
            # Either one node or None remaining
            return cur


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    _next = head.next
    head.next = swap_pairs(_next.next)
    _next.next = head

    return _next
