list=[]
number=10
for i in range(0,number):
        b=int(input("enter elements:"))
        list.append(b)
list.sort()
print("largest element",list[number-1])
