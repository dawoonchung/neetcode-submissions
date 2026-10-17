# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # [0, 1, 2, 3]
        # [0 -> 1]
        # [3, 2, 1, 0]

        # head.val = 0
        # head.next = None
        curr_head = head # 1 -> 2
        new_head = None # 0 -> None

        while curr_head:
            new_head = ListNode(curr_head.val, new_head)
            curr_head = curr_head.next
        
        return new_head