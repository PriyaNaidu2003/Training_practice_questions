s=input()
ch1=input()
ch2=input()
s=list(s)
for i in range(len(s)):
    if s[i]==ch1:
        s[i]=ch2
    elif s[i] == ch2:
        s[i]=ch1
print(''.join(s))
