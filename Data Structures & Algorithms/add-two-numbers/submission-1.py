# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        curr_sum = 0
        carry = 0
        dummy = ListNode(0)
        head = dummy

        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)

            curr_sum = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10

            dummy.next = ListNode(curr_sum)

            curr_sum = 0
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        if carry:
            dummy.next = ListNode(carry)
            
        
        return head.next



