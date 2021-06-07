class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:    
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        if self.head==None:
            new=Node(data)
            self.head=new

            #Creating link
            self.head.next=self.head
        else:
            new=Node(data)
            new.next=self.head.next
            self.head.next=new
        return self.head
    
    def insert_at_last(self,data):
        if self.head==None:
            new=Node(data)
            self.head=new

            #Creating link
            self.head.next=self.head
        else:
            new=Node(data)
            new.next=self.head.next
            self.head.next=new
            self.head=new
        return self.head  
    
    def display(self):
        if self.head==None:
            print("Empty")
        else:
            temp=self.head.next
            while temp:
                print(temp.data,end="->")
                temp=temp.next
                if temp==self.head.next:
                    print("...",temp.data)
                    break
    def swap_fl(self):
        p=self.head.next
        while p.next!=self.head:
            p=p.next
        p.data,self.head.data=self.head.data,p.data

        
        
if True:
    llist=LinkedList()
    l=[10,15,12,13,20,14]
    for i in l:
        head=llist.insert_at_front(i)
    print("All element are inserted: \n")
    llist.display()

    print("After changing first and last node")
    llist.swap_fl()
    llist.display()

