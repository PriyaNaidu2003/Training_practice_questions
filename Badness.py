p=input()
paint=list(p)
for i in range(0,len(paint)):
    if i!=len(paint)-1:
        if paint[i].lower()=='w':
            for j in range(i+1,len(paint)):
                if paint[j].lower()!='w':
                    paint[i]=paint[j]
                    break
    else:
        if paint[i].lower()=='w':
            paint[i]=paint[i-1]

print(paint)
badness=0
for  i in range(1,len(paint)):
    if paint[i]!=paint[i-1]:
        badness+=1
print(badness)


# def minimize_badness(s):
# # The problem implies that you can repaint houses to minimize the badness value.
# # If the string contains 'w', it means the house can be repainted.
# # To minimize badness, we should paint all 'w' such that the adjacent houses are the same color.
#
# # Replace all 'w' in the string
#     if 'w' in s:
#         s = s.replace('w', '')
#
#     # Calculate the badness value of the modified string
#     badness = 0
#     for i in range(1, len(s)):
#         if s[i] != s[i - 1]:
#             badness += 1
#
#     return badness
#
# # Test cases
# print(minimize_badness("www"))
