# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr_head = head
        new_head = None

        while curr_head:
            new_head = ListNode(curr_head.val, new_head)
            curr_head = curr_head.next
        
        return new_head