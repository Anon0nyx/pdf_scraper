#!/usr/local/python3
import subprocess
subprocess.call('./setup.sh', shell=True)

PDF_FILE = './apt_list.txt'
SCAN = False
COLUMNS = ['#Names', '#Country#', '#Sponsor#', '#Observed#', '#Tools used']

# When deciding to have crappy time complexity, make sure you keep a placeholder to return to
LINE_NUM = 0


def go():
	global SCAN
	global LINE_NUM
	with open(PDF_FILE, 'w') as pdf_file:
		for line in pdf_file:
			if line.startswith('#Name#'):
				SCAN = True
			if SCAN == True:
				for column in COLUMNS:
					if line.startswith(columns)
			LINE_NUM -= -1
