# stack implementation using linked list 

class node:
    def __init__(self,val):
        self.data = val
        self.next = None

class sll:
    def __init__(self,capacity=3):
        self.head = None
        self.capacity = capacity
        self.count = 0

    def push(self,val):
        if self.size() >= self.capacity:
            return print('stack overflow')
        new_node = node(val)
        new_node.next = self.head  
        self.head = new_node 
        self.count += 1  

    def pop(self):
        if self.is_empty():
            return print('stack underflow')
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data     

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def print_stack(self):
        if self.is_empty():
            return print('stack is empty...')
        temp = self.head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print()

    def top(self):
        if self.is_empty():
            return print('stack iis empty')
        print(self.head.data)
        


s = sll()
# print(s.is_empty()) ---> stack is empty 
# s.pop()  ---> stack underflow

s.push(10)
s.push(20)
s.push(30)
# s.push(40)  --> stack overflow
s.print_stack()
s.pop()
s.print_stack()
print(s.size())
s.top()