n=int(input())
val=list(map(int,input().split()))
c=1
superior=val[-1]
for i in range(len(val)-2,-1,-1):
    if val[i]>superior:
        superior=val[i]
        c+=1
print(c)
