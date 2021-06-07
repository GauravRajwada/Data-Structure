"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
def mergeTwoLists(l1, l2):
        temp=ListNode()
        tail=temp
        while True:
            if l1 is None:
                tail.next=l2
                break
            if l2 is None:
                tail.next=l1
                break
            if l1.val<=l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        return temp.next