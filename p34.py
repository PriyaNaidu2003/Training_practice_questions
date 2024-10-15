val=[5,5,5,10,20]
d={5:0,10:0,20:0}

for i in val:
    d[i]+=1
    change=i-5
    if change==15:
        if d[10]>0:
            d[10]-=1
            change-=10
    d[5]-=change//5

if d[5]<0:
    print(False)
else:
    print(True)
