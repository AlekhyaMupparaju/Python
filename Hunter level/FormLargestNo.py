list=[]
N=input()
for i in range(0,N):
    no=input()
    list.append(no)
list.sort(reverse=True)
def joinListData(list):
    result= ''
    for data in list:
        result += str(data)
    return result
print(joinListData(list))
