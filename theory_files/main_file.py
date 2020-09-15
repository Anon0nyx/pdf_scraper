import library_file
def main():
	group = library_file.threat_group()
	group.set_name('APT 1')
	group.set_country('China')
	print(group.get_name())
	print(group.get_country())

if __name__ == '__main__':
	main()
