N=input()
K=input()
List=[]
count=0
for i in range(0,N):
    new=input()
    List.append(new)
for i in range(0,N):
    n=List[i]
    if(n==K):
        count=count+1;
print count
