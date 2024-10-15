st=input()
s=0
for i in st.lower():
    s+=(ord(i)-ord('a')+1)
print(s)