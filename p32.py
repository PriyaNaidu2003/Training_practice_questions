#My method
# n=int(input())
# val=list(map(int,input().split()))
# m1=float('-inf')
# m2=float('-inf')
#
# for i in val:
#     if i>m1:
#         m2=m1
#         m1 = i
#     elif i>m2 and i!=m1:
#         m2=i
# c=0
# for i in val:
#     if i==m2:
#         c+=1
# print(c)

#val=[int(x) for x in input().split()]
#My method(2nd way because in q it is given consecutive number)
# n=int(input())
# val=list(map(int,input().split()))
# m=val[-1]
# c=0
# for i in val:
#     if i==m-1:
#         c+=1
# print(c)


#sir method
n=int(input())
val=list(map(int,input().split()))
m=val[-1]
for i in range(n-1,0,-1):
    if val[i]<m:
        print(val.count(val[i]))
        break
else:
    print(0)





