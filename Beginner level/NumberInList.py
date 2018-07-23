N=input()
K=input()
List=[]
for i in range(0,N):
    new=input()
    List.append(new)
if K in List:
    print("Yes")
else:
    print("No")
