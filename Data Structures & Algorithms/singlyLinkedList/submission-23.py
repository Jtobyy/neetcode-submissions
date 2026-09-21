class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        j = 0
        temp = self.head
        while j < index:
            temp = temp.next
            j += 1
        return temp.next.val

    def insertHead(self, val: int) -> None:
        old_head = self.head.next
        new_head = Node(val, old_head)
        self.head.next = new_head

        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.head.next = Node(val)
            self.size += 1
            return

        temp = self.head.next
        while temp.next:
            temp = temp.next
        
        temp.next = Node(val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        j = 0
        temp = self.head
        while j < index:
            temp = temp.next
            j += 1
        
        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        self.size -= 1
        return True
        
    def getValues(self) -> List[int]:
        result = []

        temp = self.head.next
        while temp:
            result.append(temp.val)
            temp = temp.next
        
        return result

        
