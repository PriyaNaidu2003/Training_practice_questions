n=int(input())
c=0
val=list(map(int,input().split()))
for i in range(len(val)-1):
    if val[i]>val[i+1]:
        c+=1
print(c)
