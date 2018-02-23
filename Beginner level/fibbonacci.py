number=int(input())
n1 = 0
n2 = 1
count = 1
fibo=[n2]
while count<number:
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
    fibo.append(n3)
print fibo
