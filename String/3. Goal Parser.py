"""
Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
"""
class Solution:
    def interpret(self, command: str) -> str:
        i=0
        ans=""
        while(i<len(command)):
            if command[i]=="G":
                ans+=command[i]
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                ans+="o"
                i+=2
            elif command[i]=="(" and command[i+1]=="a":
                ans+="al"
                i+=3
            else:
                i+=1
        return ans