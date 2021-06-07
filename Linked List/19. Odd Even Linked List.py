"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""
def oddEvenList(head):
        even=None
        etail=even
        odd=None
        otail=even
        curr=head
        while curr:
            if curr.val%2==0:
                if even is None:
                    even=etail=curr
                else:
                    etail.next=curr
                    etail=etail.next
            else:
                if odd is None:
                    odd=otail=curr
                else:
                    otail.next=curr
                    otail=otail.next
            curr=curr.next
        if head.val%2==0:
            head=even
            etail.next=odd
            otail.next=None
        else:
            head=odd
            otail.next=even
            etail.next=None
        return head