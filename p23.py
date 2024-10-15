val=list(map(int,input().split()))
val.reverse()
s=0
for i in range(len(val)):
    if i%2==0:
        s+=val[i]
print(s)
