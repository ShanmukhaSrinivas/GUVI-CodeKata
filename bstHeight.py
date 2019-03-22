class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None
        
    def add_node(self,n):
        self.temp = Node(n)
        if self.root == None:
            self.root = self.temp
            
        else:
            self.tail = self.head
           
            if self.temp.data < self.head.data
                self.tail.left = self.temp
                self.tail = self.tail.left
            else:
                self.temp.right = self.temp
                self.tail = self.tail.right
obj = LinkedList()
obj.add_node(3)
obj.add_node(2)
obj.add_node(1)
obj.add_node(5)
obj.add_node(9)
obj.add_node(0)