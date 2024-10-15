#My method
n=int(input())
val=list(map(int,input().split()))
p=-1
for i in range(1,n-1):
    if sum(val[:i])==sum(val[i+1:]):
        p=i
if p==-1:
    print(-1)
else:
    print(p)

#Sir method
#using(algorithm)

n=int(input())
val=list(map(int,input().split()))
lhs=0
rhs=sum(val)
for i in range(len(val)):
    rhs=rhs-val[i]
    if lhs==rhs:
        print(i)
        break
    else:
        lhs+=val[i]
#2nd way
n=int(input())
val=list(map(int,input().split()))
lhs=0
rhs=sum(val)
for i in val:
    rhs=rhs-i
    if lhs==rhs:
        print(val.index(i))
        break
    lhs += val[i]
else:
    print(-1)
