import library_file, time, re, csv

COLUMNS = [ 'Names', 'Country', 'Sponsor', 'Observed', 'Tools used' ]

def main():
	library_file.clean_data()

	pdf_file = open('./apt_list.txt')
	count = 0
	with open('output.csv', 'w') as out_file:
		# Setup csv writer and write header to file
		writer = csv.DictWriter(out_file, fieldnames=COLUMNS)
		writer.writeheader()
		for line in pdf_file:
			threat_actor = library_file.ThreatGroup()
			# First line is garbage
			if count == 0:
				pass
			else:
				split_line = line.split('#')
				foobar = []
				# Clean up the blank indexes within the split_line
				for item in split_line:
					if not re.match('[a-zA-Z0-9]', item) and not re.match('..', item):
						pass
					else:
						foobar.append(item)
			
				# Determine what value we are being given and determine if the next value is 
				# a field and if it is keep the object value as [UNKNOWN]
				for i in range(len(foobar)):
					if re.match('Names', str(foobar[i])) and not re.match('Country', str(foobar[i+1])):
						threat_actor.set_names(str(foobar[i+1]))
					if re.match('Country', str(foobar[i])) and not re.match('Sponsor', str(foobar[i+1])):
						threat_actor.set_country(str(foobar[i+1]))
					if re.match('Sponsor', str(foobar[i])) and not re.match('Observed', str(foobar[i+1])):
						threat_actor.set_sponsor(str(foobar[i+1]))
					if re.match('Observed', str(foobar[i])) and not re.match('Tools used', str(foobar[i+1])):
						threat_actor.set_observed(str(foobar[i+1]))
					if re.match('Tools used', str(foobar[i])):
						threat_actor.set_tools(str(foobar[i+1]))

			# Print the row to the csv file
			writer.writerow({'Names': str(threat_actor.get_names()), 'Country': str(threat_actor.get_country()), 'Sponsor': str(threat_actor.get_sponsor()), 'Observed': str(threat_actor.get_observed()), 'Tools used': str(threat_actor.get_tools()) }) 
			count -= -1
			
	# Close the file
	out_file.close()

if __name__ == '__main__':
	main()
