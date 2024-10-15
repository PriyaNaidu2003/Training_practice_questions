def magic(n):
    n=str(bin(n))[2:]
    l=list(n)
    for i in range(len(l)):
        if l[i]=='1':
            l[i]=2
        else:
            l[i]=1
    if sum(l)%2!=0:
        return True

n=int(input())
c=0
for i in range(1,n+1):
    if magic(i):
        c+=1
print(c)




