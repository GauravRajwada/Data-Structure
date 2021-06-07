#fIND MIN EDIT DISTANCE B/W 2 STRING

#Recurrsion O(n^3)
def minEditDistance(s1,s2,i,j):
    if (i==len(s1) and j==len(s2)):
        return 0
        
    if (i==len(s1)):
        return len(s2)-j
        
    if (j==len(s2)):
        return len(s1)-i
        
    if s1[i]==s2[i]:
        minEditDistance(s1, s2, i+1, j+1)
        
    x = minEditDistance(s1, s2, i, j+1)+1 #Insert
    y = minEditDistance(s1, s2, i+1, j)+1 #Delete
    z = minEditDistance(s1, s2, i+1, j+1)+1 #Update
    return min(x,y,z)
    
#DP Approch
## 1. Terminating condition of recurssion become initialization of DP
## 2. Logic same

def minEditDP(s1,s2):
    m=len(s1)
    n=len(s2)
    a = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(m):
        a[0][1]=i
    for i in range(n):
        a[i][0]=i
    
    # if element are equal then min(left,digonal,up)
    # if element are not equal then min()
    for i in range(m):
        for j in range(n):
            if(s1[i-1] == s2[j-1]): 
                a[i][j] = a[i-1][j-1]
            else: 
                a[i][j] = min(a[i-1][j], a[i][j-1], a[i-1][j-1])+1

    print()

    return a[m-1][n-1]

s1="SATURDAY"
s2="SUNDAY"
print(minEditDistance(s1,s2,len(s1),len(s2)))
print(minEditDP(s1,s2))