import re
import math
from collections import defaultdict

def str_time_to_num(hr, mn):
	hr = int(hr)
	mn = int(mn)
	if hr > 12: #assume anything after noon came the day before
		hr -= 24
	return mn + (60 * hr)
		

def num_time_to_str(num):
	hr = math.floor(num / 60)
	mn = num % 60
	return ("%02d" % hr, "%20d" % mn)

with open('4.txt') as file:
	#parse logs out of source
	logs = []
	for line in file:
		r = re.search(r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] ([\w\s#]*)", line.strip())
		log = { 'raw': r.group(0),
			'year': r.group(1),
			'mo': r.group(2),
			'day': r.group(3),
			'hr': r.group(4),
			'min': r.group(5),
			'msg': r.group(6)}
		logs.append(log)
	logs.sort(key=lambda x: int(x['year']+x['mo']+x['day']+x['hr']+x['min'])) #combining the strings and casting to int
	
	# interpret logs into guard activity
	guards = {}
	current_guard = None
	fall_asleep_time = None
	for log in logs:
		if 'Guard' in log['msg']: #shift change
			r = re.search(r"#(\d*)", log['msg'])
			current_guard = r.group(1)
		if 'falls' in log['msg']: #going to sleep
			fall_asleep_time = str_time_to_num(log['hr'], log['min'])
		if 'wakes' in log['msg']: #waking up, log the time
			if current_guard not in guards:
				guards[current_guard] = defaultdict(int)
			wakeup_time = str_time_to_num(log['hr'], log['min'])
			for minute in range(fall_asleep_time, wakeup_time):
				guards[current_guard][minute] += 1



	#search for best guard
	best_guard = None
	for key in guards:
		for hour in guards[key]:
			if best_guard is None or guards[key][hour] > guards[best_guard[0]][best_guard[1]]:
				best_guard = (key, hour)
	print(best_guard)
	print(int(best_guard[0]) * best_guard[1])


		
		
'''part 1
	max_sum = 0
	for key in guards:
		s = 0
		for count in guards[key].values():
			s += count
		if s > max_sum:
			best_guard = (key, guards[key])
			max_sum = s
		
	best_hour = (0, 0)
	for hour in best_guard[1]:
		if best_guard[1][hour] > best_hour[1]:
			best_hour = (hour, best_guard[1][hour])
	print(best_guard)
	print(best_hour)
	print('-')
	print(int(best_guard[0]) * best_hour[0])
'''




