# # #bitwise conepts
# #
# # #find even or odd using bitwise(and)
# # n=int(input())
# #
# # if n & 1 :
# #     print('Odd')
# # else:
# #     print('Even')
# #
# # #Toggle the kth bit of a number(shift and xor)
# # n=int(input())
# # k=int(input())
# #
# # s=1<<(k-1)             #0 based index
# # print(n^s)
#
# #clear the kth bit of a number
# n=int(input())
# k=int(input())
#
# s=1<<(k-1)             #0 based index
# print(n & ~s)

# toogle all the bits
import math
n=int(input())
k=int(math.log(n,2))+1  #To find the number of bits in binary form of n
k=1<<k
m=k-1
print(n^m)



