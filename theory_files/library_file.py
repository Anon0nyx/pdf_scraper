import subprocess

X = 10
Y = 5
Z = 4

def go():
	print('Hello, Friend')
	subprocess.call('./script.sh', shell=True)

def do_math():
	global X
	X = Y + Z
	print(X)
