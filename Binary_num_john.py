n=int(input())
sym=0
pow=0
temp=n
while n>0:
    sym+=(2**pow)
    print(sym)
    n=n//2
    print(n)
    pow+=1
    print(pow)
print(sym-temp)