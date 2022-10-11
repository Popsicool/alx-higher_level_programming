#!/usr/bin/python3
class Square:
	def __init__(self, size=0):
		if (isinstance(size, int) == False):
			raise TypeError('size must be an integer')
		elif (size < 0):
			raise ValueError('size must be >= 0')
		else:
			self.__size = size
	@property	
	def size(self):
		return self.__size
		
	@size.setter
	def size(self, value):
		if (isinstance(value, int) == False):
			raise TypeError('size must be an integer')
		elif (value < 0):
			raise ValueError('size must be >= 0')
		else:
			self.__size = value
			
	def area(self):
		return self.__size ** 2
	
	def my_print(self):
		if self.__size == 0:
			print()
			return
		i = 0
		while ( i < self.__size):
			j = 0
			while (j < self.__size):
				print("#", end="")
				j += 1
			print()
			i += 1
		
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")