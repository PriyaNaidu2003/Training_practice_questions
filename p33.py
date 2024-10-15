def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
s=input()
c=0
for i in s.lower():
    if i not in 'aeiou':
        c+=1
if c==0:
    print(0)
else:
    print(fact(c))


