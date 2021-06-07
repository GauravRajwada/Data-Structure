"""
The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

Example 1:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
"""

class Solution:
    def isSumEqual(self, a: str, b: str, c: str) -> bool:
        has={}
        for i in range(97,123):
            has[chr(i)]=i
        l1=[]
        l2=[]
        l3=[]
        for i in a:
            l1.append(str((has[i]-97)))
        for i in b:
            l2.append(str((has[i]-97)))
        for i in c:
            l3.append(str((has[i]-97)))

        l1=int("".join(l1))  
        l2=int("".join(l2))  
        l3=int("".join(l3))    

        if (l1+l2)==l3:
            return True
        else:
            return False