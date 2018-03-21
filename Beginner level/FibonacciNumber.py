number=int(input())
n1=0
n2=1
count=0
fibonacci=[n2]
while count<number:
    print n1
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
    fibonacci.append(n3)
