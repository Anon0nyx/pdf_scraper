import subprocess, os

class threat_group():
	def __init__(self):
		self.name = '[UNKNOWN]'
		self.country = '[UNKNOWN]'
		self.sponsor = '[UNKNOWN]'
		self.observed = '[UNKNOWN]'
		self.tools = '[UNKNOWN]'

	# Setter functions
	def set_name(self, value):
		self.name = value
	def set_country(self, value):
		self.country = value
	def set_sponsor(self, value):
		self.sponsor = value
	def set_obvserved(self, value):
		self.observed = value
	def set_tools(self, value):
		self.tools = value
	
	# Getter functions
	def get_name(self):
		return self.name
	def get_country(self):
		return self.country
	def get_sponsor(self):
		return self.sponsor
	def get_observed(self):
		return self.observed
	def get_tools(self):
		return self.tools

def clean_data():
	subprocess.call('./script.sh', shell=True)
	out_file = open('apt_list_cleaner.txt', 'w')
	in_file = open('apt_list.txt', encoding='utf8', errors='ignore')
	for line in in_file:
		out_file.write(line.strip('\n'))
	in_file.close()
	os.system("perl -i -pe's/#Names#/\n#Names#/g' apt_list_cleaner.txt")
		
