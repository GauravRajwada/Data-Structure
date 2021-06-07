"""
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
def isPalindrome(head):
        p=head
        arr=[]
        if head is None:
            return True
        elif head.next is None:
            return True
        else:
            while p.next is not None:
                arr.append(p.val)
                p=p.next
            if p.next is None:
                arr.append(p.val)
        if arr==arr[::-1]:
            return True
        else:
            return False