list=[]
newList=[]
length=input()
for i in range(0,length):
    no=input()
    list.append(no)
for i in range(0,length):
    if(list[i]==i):
        newList.append(list[i])
newLen=len(newList)
if(newLen!=0):
    newList.sort()
    print newList
else:
    print(" '-1' ")
