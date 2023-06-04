#! /usr/bin/python3.10
import os
import sys


def main():
	folder = sys.argv[1]
	array = os.walk(folder)
	count = 0

	for i in array:
		for item in i[2]:
			print(os.path.join(os.getcwd(), i[0], item), "\t", os.path.getsize(os.path.join(os.getcwd(), i[0], item)))
			count += os.path.getsize(os.path.join(os.getcwd(), i[0], item))

	print(count)

if __name__ == "__main__":
	main()