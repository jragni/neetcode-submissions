class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val) 
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node
        
        if not self.head:
            self.head = self.tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        
        curr = self.head
        i = 0
        while curr:
            print(f"curr:{curr.val}")
            if i + 1 == index and curr.next:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr 

                return True
            i += 1
            curr = curr.next
                
        return False


    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
