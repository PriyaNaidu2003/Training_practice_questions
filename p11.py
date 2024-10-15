num=input()
s=0
for i in range(len(num)):
    for j in range(i,len(num)):
        s+=int(num[i:j+1])
print(s)





