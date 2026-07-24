class node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node.prev = cur
            cur.next = new_node
    
    def traversal(self):
        if self.head is None:
            print('dll is empty.....')
        else:
            cur = self.head
            while cur:
                print(cur.val,end=" --> ")
                cur = cur.next
            print('None')

    def insert(self, val, position):
        new_node = node(val)

    # Empty list
        if self.head is None:
            if position == 0:
              self.head = new_node
            else:
               print("Invalid Position")
            return

    # Insert at beginning
        if position == 0:
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node
           return

        cur = self.head
        count = 0

        while cur and count < position:
            cur = cur.next
            count += 1

        if count != position:
            print("Invalid Position")
            return

        if cur is None:  # Insert at end
            tail = self.head
            while tail.next:
              tail = tail.next
            tail.next = new_node
            new_node.prev = tail
        else:  # Insert in middle
           prev = cur.prev
           prev.next = new_node
           new_node.prev = prev
           new_node.next = cur
           cur.prev = new_node
    
    def delete(self,val):
        if self.head is None:
            print('dll is empty...')
            return 
        if self.head.val == val:
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            del temp
        
        cur = self.head
        while cur:
                if cur.val == val:
                    
                    if cur.next:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                    else:
                        cur.prev.next = None
                    del cur
                    return 
                cur = cur.next
        print('not found')
        

dll = dll()

dll.append(5)
dll.append(10)
dll.append(12)
dll.append(15)    
dll.insert(4,4)
# dll.insert(10,0)
# dll.append(20)
# dll.insert(30,1)
# dll.insert(100,4)
# dll.delete(100)
# dll.append(55)
# dll.append(56)
# dll.delete(55)
# dll.delete(56)

dll.delete(4)

dll.traversal()