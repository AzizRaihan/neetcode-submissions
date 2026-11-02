# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None

        while curr:
            nxt=curr.next #2
            curr.next=prev #1 to 2

            prev=curr #1 to none 
            curr=nxt

        return prev
        
        