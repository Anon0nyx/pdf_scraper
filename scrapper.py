#!/usr/local/bin/python3

import time, csv
import organize_data as fix_data

COLUMNS = [ 'Name', 'Country', 'Sponsor', 'Observed', 'Tool used' ]

NAMES = []
COUNTRIES = []
SPONSORS = []
OBSERVED = []
TOOLS = []

LENGTH = 0

PRIMARY_FILE = './apt_list.txt'
COUNTRY_FILE = './tmp/countries.temp'

DEBUG = True

def collect_single_line(field_file):
	alist = []
	for line in open(field_file, encoding='utf8', errors='ignore'):
		alist.append(line.strip('\n'))
	return alist

def collect_block_text(current_field, next_field):
	global collect
	return_list = []
	string = ''
	collect = False
	idx = 0
	with open(PRIMARY_FILE, encoding='utf8', errors='ignore') as in_file:
		for line in in_file:
			if line.startswith(current_field):
				string = ''
				collect = True
			elif line.startswith(next_field):
				if string not in return_list:
					return_list.append(string)
				else:
					continue
			elif line.startswith('#') and not line.startswith(next_field):
				# CONTINUE HERE				
			if collect == True:
				string += line
			idx += 1
	return return_list

def move_data():
	with open('output.csv', 'w') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=COLUMNS)

		writer.writeheader()
		for i in range(LENGTH):
			writer.writerow({'Name': NAMES[i], 'Country': COUNTRIES[i], 'Observed': OBSERVED[i], 'Tool used': TOOLS[i]})

def main():
	fix_data.go()
	time.sleep(3)
	
	global LENGTH
	global NAMES
	global COUNTRIES
	global SPONSORS
	global OBSERVED
	global TOOLS
	
	NAMES = collect_block_text('#Names#', '#Country#')
	COUNTRIES = collect_single_line(COUNTRY_FILE)
	SPONSORS = collect_block_text('#Sponsor#')
	OBSERVED = collect_block_text('#Observed#')
	TOOLS = collect_block_text('#Tools used#')
	
	LENGTH = len(NAMES)
	
	if DEBUG == True:
		for i in range(len(COUNTRIES)):
			print('[' + COUNTRIES[i] + ']', i)
		print(len(NAMES))
		print(len(COUNTRIES))
		print(len(SPONSORS))
		print(len(OBSERVED))
		print(len(TOOLS))
	else:
		move_data()

if __name__ == '__main__':
	main()

