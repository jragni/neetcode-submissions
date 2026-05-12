# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: 
            return False
        
        curr = head
        n = head.next

        while n:
            print(f'curr: {curr.val} n: {n.val}')
            if curr == n:
                return True
            
            curr = curr.next

            if not n.next:
                return False

            n = n.next.next
        
        return False
        