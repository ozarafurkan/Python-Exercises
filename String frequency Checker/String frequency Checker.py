mystring=input()
mydict=dict()
for i in mystring:
    if (i in mydict):
        mydict[i]+=1
    else:
        mydict[i]=1
for i,j in mydict.items():
    print(i,j)
