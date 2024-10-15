#My way
# s1=input("enter s1")
# s2=input("enter s2")
# s3=''
# n=len(s1)+len(s2)
# i=0
# while i<n:
#     if i>len(s1)-1:
#         s3+=s2[i:]
#         break
#     elif i>len(s2)-1:
#         s3 += s1[i:]
#         break
#     else:
#         s3 = s3 + s1[i] + s2[i]
#     i+=1
# print(s3)

#sir method
s1=input()
s2=input()
res='';i=0
while i<len(s1) or i<len(s2):
    if i<len(s1):
        res+=s1[i]
    if i < len(s2):
        res += s2[i]
    i+=1
print(res)







