#My method
s=input()
sm=0
i=0
while i<=len(s)-1:
    if s[i].isdigit() :
        if s[i+1].isdigit():
            sm+=(int(s[i]+s[i+1]))
            i=i+2
        else:
            sm += (int(s[i]))
    i=i+1
print(sm)
#Sir method
s=input()
num=0;res=0
for i in s:
    if i.isdigit():
        num=num*10+int(i)
    else:
        res+=num
        num=0
res+=num
print(res)










