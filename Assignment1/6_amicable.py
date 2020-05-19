'''Find the first 10 pairs of amicable numbers.'''

import math

def factors(n):
	fsum = 0
	i = 2
	while i <= math.sqrt(n) :
		if n % i == 0 :
			if n // i == i :
				fsum += i
			else :
				fsum += i
				fsum += n // i
		i += 1
	return fsum + 1

if __name__ == '__main__' :
	count = 0
	num1 = 2
	ami = []
	while count < 10 :	
		fsum = factors(num1)
		num2 = factors(fsum)
		if num1 == num2 :
			if num1 != fsum :
				ami.append((num1, int(fsum)))
				count += 1
			
		num1 += 1
		
		for i in ami :
			if num1 == i[0] or num1 == i[1] :
				num1 += 1
	print(ami)
	
	
