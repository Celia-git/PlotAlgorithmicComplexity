class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def Append(self, num:int):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            new_node.prev = None
            new_node.next = None
        else:
            temp = self.head                
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def ArrayToList(self, nums:list):
         #This is just an appending function on a loop
        for x in nums:
            new_node = Node(x)
            if self.head == None:
                self.head = new_node
                new_node.prev = None
                new_node.next = None
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp
            
    def Display(self)->list:
        current = self.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        return values
        
    def DisplayReverse(self)->list: #Testing prev on the nodes
        current = self.head
        values = []
        while current.next != None:
            current = current.next
        while current:
            values.append(current.data)
            current = current.prev
        return values
        
    def Insert(self, num:int):
        new_node = Node(num)
        
        if self.head == None or new_node.data <= self.head.data:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None and temp.next.data < new_node.data):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp 
            if new_node.next != None:
                new_node.next.prev = new_node

    def __str__(self) -> str:
        return str(self.Display())

class Node:
    def __init__(self, data:int): 
        self.data = data
        self.next = None
        self.prev = None   

''' ------------------------------------ TESTING ----------------------------------------

Asdf = DoublyLinkedList()
A = [43, 87, 20, 6, 54]
Asdf.ArrayToList(A)
Asdf.Display()
Asdf.DisplayReverse()


Jkl = DoublyLinkedList()
B = [8, 17, 29, 43, 67, 80, 96, 100]
print("Array to List:")
Jkl.ArrayToList(B)
Jkl.Display()
print("Inserting 12")
Jkl.Insert(12)
Jkl.Display()
print("Inserting 50")
Jkl.Insert(50)
Jkl.Display()
print("Inserting 123")
Jkl.Insert(123)
Jkl.Display()
print("Inserting 5")
Jkl.Insert(5)
Jkl.Display()
print("Inserting 10")
Jkl.Insert(10)
Jkl.Display()
print("Printing in Reverse")
Jkl.DisplayReverse()
'''