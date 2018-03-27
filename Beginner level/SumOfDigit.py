number=int(input(''))
newNum=number
sum=0
while(newNum!=0):
    rem=newNum%10
    sum=sum+rem
    newNum=newNum/10
print(sum)
