time1 = input()
hour1= time1 //60
time1 %= 60
minutes1 = time1 // 1
time2=input()
hour2=time2//60
time2%=60
minutes2=time2//1
print("h:m-> %d:%d" % (hour1,minutes1))
print("h:m-> %d:%d" % (hour2,minutes2))
result=hour1-hour2
resut2=minutes1-minutes2
print("Result is h:m-> %d:%d" % (result,resut2))
