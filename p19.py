#my way
s1=input()
s2=input()
c=0
for i in s1:
    if i in s2:
        c+=1
print(len(s2)-c)


#sir method
s1=input()
s2=input()
l=list(s2)
for i in l:
    if i in s1:
        l.remove(i)
print(len(l))