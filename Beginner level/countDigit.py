def countfun(number):
	count=0
	while(number!=0):
		number//=10
		count=count+1
	print(count)
def main():
	try:
		number=int(input())
		countfun(number)
	except:
		print('invalid')
main()
