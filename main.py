

# inital value
value = 0
store = {0: True}
run_count = 0

with open('1.txt') as fp:
	while True:
		for line in fp:
			num = int(line)
			value += num
			if value in store:
				print('Found it!')
				print(value)		
				exit()
			store[value] = True
	#		print(store)
		print('loop done')
		fp.seek(0) #reset filehandler
		run_count+=1
		print(run_count)
		print(len(store))
