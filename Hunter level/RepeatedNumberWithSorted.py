list=[]
N=input()
for i in range(0,N):
    no=input()
    list.append(no)
final_list = []
for num in range(0,N):
    i=num+1
    for i in range(i,N):
        if list[num]== list[i]:
            if num  in final_list:
                break;
            else:        
                final_list.append(list[num])
final_list.sort()
print final_list
