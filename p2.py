

st=input()
st1=''
for i in st:
    v=97+(122-ord(i))
    st1+=chr(v)
print(st1)