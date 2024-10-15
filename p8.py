s=input()
st=''
s=s.split('0')
for i in s:
    st+=(chr(64+len(i)))
print(st)


