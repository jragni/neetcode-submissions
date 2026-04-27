# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list in half by using slow/fast pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        second = self.reverse(slow.next)
        slow.next = None

        # create a dummy list node
        dummy = ListNode(0)
        first = head
        res = dummy
        
        while first and second:
            dummy.next = first
            first = first.next
            dummy = dummy.next
            dummy.next = second
            second = second.next
            dummy = dummy.next

        if first:
            dummy.next = first

        if second:
            dummy.next = second
    

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
           temp =  curr.next
           curr.next = prev
           prev = curr
           curr = temp

        return prev
    