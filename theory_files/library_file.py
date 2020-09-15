class threat_group():
	def __init__(self):
		self.name = None
		self.country = None
		self.sponsor = None
		self.observed = None
		self.tools = None

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

test = threat_group()
