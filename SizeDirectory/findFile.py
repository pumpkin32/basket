#! /usr/bin/python3.10
import os
import sys


def main():
	folder = sys.argv[1]
	file = sys.argv[2]
	array = os.walk(folder)
	count = len(file)
	
	for i in array:
		for item in i[2]:
			
			if item[-count:] == file:
				print(os.path.join(os.getcwd(), i[0], item))
			else:
				continue


if __name__ == "__main__":
	main()