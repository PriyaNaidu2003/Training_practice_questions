st=input()
st1=''
for i in st:
    if ord(i) in range(97,119): #if (ord(i)<ord('v')):
        v=ord(i)+5
    else:
        v=ord(i)+5-26

    st1+=chr(v)
print(st1)