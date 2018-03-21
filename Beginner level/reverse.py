number=int(input(''))
reverse=0
while(number!=0):
    reminder=number%10;
    reverse=(reverse*10)+reminder;
    number/=10;
print reverse
