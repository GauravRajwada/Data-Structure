
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:    
    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
        return self.head
    
    def display(self):
        p=self.head
        while p!=None:
            print(p.data)
            p=p.next
        
if True:
    llist=LinkedList()
    l=[10,15,12,13,20,14]
    for i in l:
        head=llist.insert_at_start(i)
    print("All element are inserted: \n")
    llist.display()


