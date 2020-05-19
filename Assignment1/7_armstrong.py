'''Find Armstrong Numbers in the given range.'''

ran = input('Enter the numbers in range separated by a space : \n').split()
s = int(ran[0])
e = int(ran[1])
if s < e:
	lst = []
	print('The Armstrong numbers in the range %d and %d are :' %(s, e))
	for i in range(s, e + 1):
		sum_ = 0
		j = i
		while j:
			r = j % 10
			j = j // 10
			sum_ = sum_ + r**3
		if sum_ == i:
			lst.append(i)
	print(lst)

else:
	print('Incorrect input!')

