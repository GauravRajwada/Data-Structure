
class Node:
    def __init__(self,data=0):
        self.data=data
        self.left=None
        self.right=None

def createBST(queue):
    pass

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right,end=" ")


if __name__=='__main__':
    queue=[1,2,3,4,5]
    root=createBST(queue)
    in_order(root)