'''Find the first 10 harmonic divisor numbers.'''

def factors(num) :
	lst = []
	for i in range(1, num + 1) :
		if num % i == 0 :
			lst.append(i)
	mean = harmonic(lst, len(lst))
	return mean


def harmonic(lst, n) :
	hsum = 0
	for i in lst :	
		hsum = hsum + (1.0 / i)
	return (n / hsum)
	
	
if __name__ == '__main__' :
	i = 1 
	count = 0
	har = []
	while count < 10 :
		harmonic_mean = round(factors(i), 5)
		if harmonic_mean.is_integer() :
			har.append(i)
			count += 1
		
		i += 1
		
	print("First 10 Harmonic Divisor numbers are :", har)
