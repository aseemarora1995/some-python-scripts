import os
from os.path import isfile, join

def main():
	my_path = '/home/aseemarora/Videos/Jikai Tang/'
	# os.chdir(my_path)
	# print os.getcwd()
	for filename in os.listdir(my_path):
		if isfile(join(my_path, filename)):
			print filename
			close = filename.find(']')
			start = 10
			print close-start
			if close-start>0:
				if close-start == 2:
					os.rename(my_path+filename, my_path+filename[:10]+'0'+filename[10:])
				elif close-start == 1:
					os.rename(my_path+filename, my_path+filename[:10]+'00'+filename[10:])
			# newname = filename[7:]
			# os.rename(my_path+filename, my_path+'['+filename)
			# print filename


if __name__ == '__main__':
	main()