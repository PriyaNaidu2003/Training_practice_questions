#august(2024)
#My Method
n=int(input())
n=str(bin(n))
k=n.count('1')
s=0
for i in range(k):
    s+=2**i
print(s)


# sir method
n=int(input())
b=str(bin(n))[2:]
s1='';s2=''
for i in b:
    if i in b:
        s1+=i
    else:
        s2+=i
res=s1+s2
k=0;sum=0;i=len(res)-1
while i>=0:
    sum+=int(res[i])*2**i
    i-=1
print(sum)



