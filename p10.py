#My method
# val=list(map(int,input().split()))
# l=[]
# c=0
# for i in range(len(val)):
#     if val[i]!=0:
#         c+=1
#         l.append(val[i])
# for i in range(len(val)-c):
#     l.append(0)
# print(l)

#sir method
val=[4,5,0,1,9,0,5,0]
res1=[];res2=[]
for i in val:
    if i==0:
        res1.append(i)
    else:
        res2.append(i)
res=res2+res1
print(res)








