import sys
sys.setrecursionlimit(100000)
import time

def letters_reaction(a, b):
	r = letter_to_ordinal(a) + letter_to_ordinal(b)
	return r
	

def letter_to_ordinal(a):
	n = ord(a.upper()) - 64 # to 1-26
	if a == a.upper(): #upper case are negative polarity
		n *= -1
	return n

def recursive_eliminate_matches(p):
	for i, x in enumerate(p):
		if i > 0 and letters_reaction(p[i-1], x) == 0:
			del p[i]
			del p[i-1]
			return recursive_eliminate_matches(p)
	return p			


def old_dumb_eliminate_matches(p):
	while True:
		new_p = eliminate_first_match(p)
		if new_p is False:
			return p
		p = new_p

def eliminate_first_match(p):
	for i, x in enumerate(p):
		if i > 0 and letters_reaction(p[i-1], x) == 0:
			del p[i]
			del p[i-1]
			return p
	return False


def eliminate_matches(p):
	i = 0
	try:
		while True:	
			if letters_reaction(p[i], p[i+1]) == 0:
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
	p = eliminate_matches(p)
	print(len(p))
	
	print(time.time() - start)
