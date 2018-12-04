# hash guid into dictionary w/ counts
from collections import defaultdict

two_count = 0
three_count = 0

with open('2.txt') as file:
	for line in file:
		guid = line.strip()
		hash_dict = defaultdict(int)
		for letter in guid:
			hash_dict[letter] += 1
		if 2 in hash_dict.values():
			two_count += 1
		if 3 in hash_dict.values():
			three_count += 1

print('done')
print(two_count)
print(three_count)
print('checksum:')
print(two_count * three_count)



# brute force. A more elegant option might be binary elimination/masking/binning?
def check_letters(first_guid, second_guid):
	different = False
	for i in range(len(first_guid)):
		first_letter = first_guid[i]
		second_letter = second_guid[i]
		if first_letter is not second_letter:
			if different is True:
				return False #found a second difference
			different = True
	return different

def print_solution(first_guid, second_guid):
	

with open('2.txt') as file:
	lines = file.readlines()
	guids = [x.strip() for x in lines]
	print(guids)
	while guids:
		guid = guids.pop()
		for check_guid in guids:
			if check_letters(guid, check_guid):
				print('FOUND IT!')
				print(guid)
				print(check_guid)
				exit()
	print('no results :(')
