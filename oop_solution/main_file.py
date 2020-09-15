import library_file, time
def main():
	print('Cleaning Data')
	library_file.clean_data()
	time.sleep(3)

	pdf_file = open('./apt_list.txt')
	count = 0
	for line in pdf_file:
		print(line.split('#'))

if __name__ == '__main__':
	main()
