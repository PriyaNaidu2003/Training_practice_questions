s=input()
p=1
for i in s:
    if i.isdigit():
        p*=int(i)
print(p)