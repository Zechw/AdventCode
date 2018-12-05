import time

def letters_react(a, b):
	if a == b:
		return False
	if a.upper() != b.upper():
		return False
	return True
	

def letter_to_ordinal(a):
	# 1 to 26
	return ord(a.upper()) - 64

def eliminate_matches(p):
	i = 0
	try:
		while True:	
			if letters_react(p[i], p[i+1]):
				del p[i+1]
				del p[i]
				if i > 0:
					i -= 1 # check the new pair behind the match
			else: 
				i += 1
	except IndexError:
		return p	


start = time.time()
with open('5.txt') as file:
	p = file.read().strip()
	p = [x for x in p]
	for n in range(1,27):
		np = [x for x in p if letter_to_ordinal(x) != n]
		np = eliminate_matches(np)
		print('-')
		print(n)
		print(len(np))
	
	print(time.time() - start)
