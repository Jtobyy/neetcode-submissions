class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.HEAD = None
        self.TAIL = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size: 
            return -1
        if index == 0:
            return self.HEAD.val

        temp = self.HEAD.next
        i = 1
        while temp:
            if index == i:
                return temp.val
            i += 1
            temp = temp.next
        

    def insertHead(self, val: int) -> None:
        node = Node(val, self.HEAD)
        if self.size == 0:
            self.TAIL = node
        self.HEAD = node
        self.size += 1
        
    def insertTail(self, val: int) -> None:
        node = Node(val, None)
        if self.size == 0:
            self.HEAD = node
            self.TAIL = node
            self.size += 1
            return
        self.TAIL.next = node
        self.TAIL = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size or index < 0:
            return False
		
        if index == 0:
            self.HEAD = self.HEAD.next
            self.size -= 1
            return True

        temp1 = self.HEAD
        temp2 = self.HEAD.next

        for i in range(0, self.size):
            if i == index - 1:
                temp1.next = temp2.next
                if temp1.next == None:
                    self.TAIL = temp1
                self.size -= 1
                return True
			
            temp1 = temp2
            temp2 = temp2.next			
		
    def getValues(self) -> List[int]:
        arr = []
        temp = self.HEAD
		
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr
