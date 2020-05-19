'''Build an application that can be used to block certain websites from opening.'''

import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

sites = int(input('How many sites you want to block?\n'))

for i in range(1, sites + 1) :
	lst = []
	website = input('Enter the site url to block : ')
	lst.append(website)
	
time_int = input('Enter the time interval during which you want to block the site separated by a space : ').split()

start = int(time_int[0])
end = int(time_int[1])

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, start) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end) :
		with open(hosts_path, 'r+') as file :
			content = file.read()
			for web in lst :
				if web in content:
					pass
				else :
					file.write(redirect + " " + web + "\n")					
	else : 
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content :
				if not any(web in line for web in lst) :
					file.write(line)
			file.truncate()			
	time.sleep(5) 
	
	
