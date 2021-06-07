def maxPower(no,a):
    while(no%a==0):
        no=no/a
    return no

def isugly(no):
    no=maxPower(no,2)
    no=maxPower(no,3)
    no=maxPower(no,5)
    if no==1:
        return 1
    else:
        return 0

n=int(input())
i=1
c=1
while c<n:
    i+=1
    if isugly(i):
        c+=1
print(i)