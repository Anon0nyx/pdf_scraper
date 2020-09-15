import subprocess, os

# Create class which represents a threat group with a threat 
# groups basic characteristics for the sake of this task
class ThreatGroup():
	def __init__(self):
		self.names = '[UNKNOWN]'
		self.country = '[UNKNOWN]'
		self.sponsor = '[UNKNOWN]'
		self.observed = '[UNKNOWN]'
		self.tools = '[UNKNOWN]'

	# Setter functions
	def set_names(self, value):
		self.names = value
	def set_country(self, value):
		self.country = value
	def set_sponsor(self, value):
		self.sponsor = value
	def set_observed(self, value):
		self.observed = value
	def set_tools(self, value):
		self.tools = value
	
	# Getter functions
	def get_names(self):
		return self.names
	def get_country(self):
		return self.country
	def get_sponsor(self):
		return self.sponsor
	def get_observed(self):
		return self.observed
	def get_tools(self):
		return self.tools

# Function to clean data
def clean_data():
	subprocess.call('./script.sh', shell=True)
	out_file = open('apt_list_cleaner.txt', 'w')
	in_file = open('apt_list.txt', encoding='utf8', errors='ignore')
	for line in in_file:
		out_file.write(line.strip('\n'))
	in_file.close()
	os.system("perl -i -pe's/#Names#/\n#Names#/g' apt_list_cleaner.txt")
	os.system("cp apt_list_cleaner.txt apt_list.txt")
	os.system("rm apt_list_cleaner.txt ../apt_list.txt")
