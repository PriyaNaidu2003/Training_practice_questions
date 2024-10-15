s=input()
cl=0
cu=0
for i in s:
    if i.islower():
        cl+=1
    elif i.isupper():
        cu+=1
if cl>cu:
    print(s.lower())
else:
    print(s.upper())