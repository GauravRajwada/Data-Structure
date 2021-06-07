"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(l1, l2):
        n1=[]
        n2=[]
        curr=l1
        while curr:
            n1.append(curr.val)
            curr=curr.next
        curr=l2
        while curr:
            n2.append(curr.val)
            curr=curr.next
        N=[]
        carry=0
        size=0
        if len(n1)>len(n2):
            size=len(n2)    
        else:
            size=len(n1)
        for i in range(size):
            s=n1.pop()+n2.pop()+carry
            carry=s//10
            N.append(s%10)
        if len(n1)>len(n2):
            for i in range(len(n1)):
                s=n1.pop()+carry
                carry=s//10
                N.append(s%10)
        else:
            for i in range(len(n2)):
                s=n2.pop()+carry
                carry=s//10
                N.append(s%10)
        if carry !=0:
            N.append(carry)
                
        N=N[::-1]
        h1=tail=None
        for i in N:
            if h1==None:
                h1=ListNode(i)
                tail=h1
            else:
                tail.next=ListNode(i)
                tail=tail.next
        head=h1
        return head