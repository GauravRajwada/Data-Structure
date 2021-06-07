class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        return Node(data)
    else:
        if data<root.data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
    return root

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data,end=" ")
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data,end=" ")

def search(root,key):
    if root is None:
        return "Not Found"
    if root.data==key:
        return "Found"
    else:
        if key<root.data:
            return search(root.left,key)
        else:
            return search(root.right,key)
    
def in_order_successor(root):
    curr=root
    while curr.left is not None:
        curr=curr.left
    return curr

def delete(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        else:
            temp=in_order_successor(root.right)
            root.data=temp.data
            root.right=delete(root.right,temp.data)
    return root
if __name__=="__main__":
    #queue=[45,39,12,10,34,32,56,54,78,67,89,81]
    queue=[50,30,20,40,70,60,80]
    root=Node(queue[0])
    for i in range(1,len(queue)):
        root=insert(root,queue[i])
    #sprint("\nInOrder:",end=" ")
    print(in_order(root))
    #print("\nPostOrder:",end=" ")
    #print(post_order(root))
    #key=800
    #print("\n",search(root,key))
    root=delete(root,20)
    print()
    in_order(root)
    root=delete(root,30)
    print()
    in_order(root)
    print()
    root=delete(root,50)
    in_order(root)