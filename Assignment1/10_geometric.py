'''Find the first 10 numbers from geometric series.'''

def geometric(a, r) :
	terms = []
	for i in range(10) :
		n = a * r**i
		terms.append(n)
	return terms
	
if __name__ == '__main__' :
	geo = input('Enter first term(a) and common ratio(r) separated by a space : \n').split()
	a = float(geo[0])
	r = float(geo[1])
	terms = geometric(a, r)
	print('First 10 numbers of the geometric series with first term = %.2f and common ratio = %.2f are:' %(a, r))
	print(terms)
