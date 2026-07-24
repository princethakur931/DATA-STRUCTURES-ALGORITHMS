# create new node
class node:
    def __init__(self,val):
        self.data = val
        self.next = None

class sll:
    def __init__(self):
        self.head = None

# insert new node at end of sll
    def append(self,val):
        new_node = node(val)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

# traversal the sll
    def traversal(self):
        if self.head == None:
            print("SLL is Empty!!")
        else:
            cur = self.head
            while cur:
                print(cur.data,end=" ---> ")
                cur = cur.next
            print('None')

# insert new node at given position

    def insert(self,position,val):
        new_node = node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = None
            cur = self.head
            count = 0
            while cur and count < position:
                prev = cur
                cur = cur.next
                count += 1
            prev.next = new_node
            new_node.next = cur
    
# delete a node from linkedlist
    def delete(self,data):
        if self.head is None:
            print("deletion is not allowed bcz linkedlist is empty.")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return 
        prev = None
        cur = self.head
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if cur is None:
            print(f"{data} not foun in linkedlist")
            return
        prev.next = cur.next
        del cur


l = sll()
l.append(5)
l.append(10)
# l.append(15)
l.append(20)

# l.insert(4,12)
# l.delete(20)
# l.delete(5)
# l.delete(12)
# l.append(65)

#l.delete(150)
l.delete(10)
l.delete(50)
l.traversal()