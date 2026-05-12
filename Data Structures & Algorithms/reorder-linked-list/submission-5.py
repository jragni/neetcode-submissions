# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)  # dummy.next is the return value
        # find length by using two pointers
        curr, n = head, head.next

        if not curr or not n:
            return 

        # split in half by using slow fast two pointers
        while n and n.next:
            curr = curr.next
            n = n.next.next
            print('breaks here in reorder')

        # get second half start  e.g. curr.next

        # reverse second half
        second_half = curr.next
        curr.next = None
        second_half = self.reverse(second_half)

        # merge lists
        self.merge(head, second_half)

    def reverse(self, head):
        if not head:
            return head
        
        curr = head
        prev = None
        temp = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def merge(self, head1, head2):
        t1 = head1
        t2 = head2
        dummy = ListNode(next=t1)
        print(f'{dummy.next.val}')

        while t1 and t2:
            temp1, temp2= t1.next, t2.next
            t1.next = t2
            t2.next = temp1
            t1, t2 = temp1, temp2
            
        
        print(f'{dummy.next.val}')
        return dummy.next


