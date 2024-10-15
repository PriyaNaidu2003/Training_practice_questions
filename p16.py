val=list(map(int,input().split()))

l=[0]*len(val)
for i in range(len(val)):
    for j in range(i+1,len(val)):
        if val[i]<val[j]:

            l[i]=j-i
            break

print(l)



