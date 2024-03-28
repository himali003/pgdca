#tuple

thislist=("pass","fail","atkt","pass")
thislist1=list(thislist)
thislist1[0]="covid"
thislist=tuple(thislist1)
print(thislist)
for i in thislist:
    print(i)
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1
c=thislist.count("pass")
print(c)
i=thislist.index("pass")
print(i)