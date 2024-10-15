def fib(n):
    if n==1 or n==0:
        return n
    else:
        return fib(n-1)+fib(n-2)
st = input()
s = 0
for i in st.lower():
    v= (ord(i) - 97)
    s+=fib(v)
print(s)