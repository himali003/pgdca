thislist=["pass","fail","atkt"]
thislist.append("covid pass")
thislist.remove("fail")
print(thislist)
for i in thislist:
    print(i)
print (len(thislist))
print (type(thislist))
print(thislist[0])
thislist[0]="fail"
print(thislist[0])
i=0
while i < len (thislist):
    print (thislist[i])
    i=i+1