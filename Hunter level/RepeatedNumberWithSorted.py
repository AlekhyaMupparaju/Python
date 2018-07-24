list=[]
final_list = []
N=input()
for i in range(0,N):
    no=input()
    list.append(no)
for num in range(0,N):
    i=num+1
    for i in range(i,N):
        if list[num]== list[i]:
            if num  in final_list:
                break;
            else:        
                 final_list.append(list[num])
fLen=len(final_list)
if(fLen!=0):
    final_list.sort();
    print final_list
else:
    print("unique")
