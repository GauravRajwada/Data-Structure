class Node:
    def __init__(self,data) :
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data <self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data     

    def search(self,key):
        if key<self.data:
            if self.left is None:
                return "Not found"
            return self.left.search(key)
        elif key>self.data:
            if self.right is None:
                return "Not found"
            return self.right.search(key)
        else:
            return "Found"


 
    
    def pre_order(self,root):
        result=[]
        if root:
            result.append(root.data)
            result+=self.pre_order(root.left)
            result+=self.pre_order(root.right)
        return result
    
    def in_order(self,root):
        result=[]
        if root:
            result=self.in_order(root.left)
            result.append(root.data)
            result+=self.in_order(root.right)
        return result

    def post_order(self,root):
        result=[]
        if root:
            result=self.post_order(root.left)
            result+=self.post_order(root.right)
            result.append(root.data)
        return result
    


if __name__=="__main__":
    queue=[45,39,12,10,34,32,56,54,78,67,89,81]
    root=Node(queue[0])
    for i in range(1,len(queue)):
        root.insert(queue[i])
    print("PreOrder:",end=" ")
    print(root.pre_order(root))
    print("\nInOrder:",end=" ")
    print(root.in_order(root))
    print("\nPostOrder:",end=" ")
    print(root.post_order(root))
    key=800
    print("\n",root.search(key))

