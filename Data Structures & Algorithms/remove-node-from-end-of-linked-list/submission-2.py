# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get count of length
        length = self.getLength(head)
        position_to_remove = length - n

        # check if removing at the beginning
        if position_to_remove == 0:
            temp = head.next
            head.next = None

            return temp

        curr = head
        i = 0
        while curr:
            if i + 1 == position_to_remove:
                curr.next = curr.next.next
            curr = curr.next
            i += 1

        return head

        
    def getLength(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count