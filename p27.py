def isPrime(n):
    if n<=1:
        return False
    i=2
    while(i*i<n):
        if n%i==0:
            return False
        i+=1
    if(i*i>n):
        return True
n=int(input())
s=0
while n>0:
    rem=n%10
    s+=rem
    n//=10
if isPrime(s):
    print('Yes')
else:
    print('No')
        