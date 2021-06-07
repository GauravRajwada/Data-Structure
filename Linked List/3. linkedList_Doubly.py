class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Dlinklist:
    def __init__(self):
        self.head=None

    def insert_at_start(self,data):
        if self.head is None:
            new=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
        return self.head
    def insert_at_last(self,data):
        if self.head is None:
            new=Node(data)
            self.head=new
        else:
            new=Node(data)
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new
            new.prev=curr
        return self.head
    
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            curr=self.head
            while curr:
                
                print(curr.data,end="<->")
                curr=curr.next

if __name__=="__main__":
    dlink=Dlinklist()
    l=[1,2,3,4,5,6,7,8,9]
    for i in l:
        head=dlink.insert_at_last(i)
    dlink.display()







