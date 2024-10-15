s=input()
k=int(input())
m=float('-inf')
for i in range(len(s)-k+1):
    p=s[i:i+k]
    if p.count('a')>m:
        m=p.count('a')
print(m)