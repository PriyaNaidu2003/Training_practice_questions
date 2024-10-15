'''here Else block belongs to For loop which exeutes
each time when for loop does work'''
val=list(map(int,input().split()))
l=[]
if len(val)==0:
    print('Null')
else:
    for i in range(len(val)):
        for j in range(i+1,len(val)):
            if val[j]<val[i]:
                l.append(val[j])
                break

        else:
            l.append(-1)
    print(*l)

