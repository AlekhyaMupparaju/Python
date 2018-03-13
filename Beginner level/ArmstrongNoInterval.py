lowerNumber =int(input(''))
upperNumber =int(input(''))
for number in range(lowerNumber,upperNumber+1):
   order = len(str(number))
   sum = 0
   temp = number
   while temp > 0:
       digit = temp%10
       sum += digit ** order
       temp //= 10
   if number == sum:
       print(number)
