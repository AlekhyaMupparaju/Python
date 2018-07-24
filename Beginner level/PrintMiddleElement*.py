myString=raw_input("")
length=len(myString)
middle=length/2
for i in range(0,length):
    if(i==middle):
        print("*")
    else:
        print myString[i]
