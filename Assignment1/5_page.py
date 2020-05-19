'''Find a missing page number from given page number list of a 25-page book for example : page number list is [2, 4-6, 12, 16, 17, 20, 21].'''

def expand(pages) :
	pages_list = []
	for page in pages :
		if '-' in page :
			j = page.split('-')
			pages_list.extend(range(int(j[0]), int(j[1]) + 1))
		
		else :
			pages_list.append(int(page))
	return pages_list
	

def missing(pages_list) :
	missing = []
	for x in range(1, 26) :	
		if x not in pages_list :
			missing.append(x)
	return missing
	
	
if __name__ == '__main__' :
	p = input('Enter the given page number list separated by a space :\n').split()
	pages_list = expand(p)
	missing_pages = missing(pages_list)
	print('The missing pages are :', missing_pages)
