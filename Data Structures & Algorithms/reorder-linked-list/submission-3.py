# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the half way point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        second = self.reverse(slow.next)

        # detach first half from second half
        slow.next = None

        # merge list
        first = head

        while first and second:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
    

    def reverse(self, head):
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev