# #My way
# st=input()
# d={}
# for i in st:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for val,key in d.items():
#     print(f"{val}:{key}")
#1st way
st=input()
st1=""
for i in st:
    if i not in st1:
        st1=st1+i
for i in st1:
    c=st.count(i)
    print(i,':',c)
    
#2nd way
st=input()
d={}
for i in st:
    d[i]=st.count(i)
for i in d:
    print(i,':',d[i])