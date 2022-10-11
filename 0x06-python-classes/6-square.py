#!/usr/bin/python3
class Square:
	def __init__(self, size=0, position=(0, 0)):
		if (isinstance(size, int) == False):
			raise TypeError('size must be an integer')
		elif (size < 0):
			raise ValueError('size must be >= 0')
		else:
			self.__size = size
		self.__position = position
			
	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, value):
		if (isinstance(value, tuple)== False and (value[0] > 0 and value[1] > 0)):
			self.__position= value
		else:
			raise TypeError("position must be a tuple of 2 positive integers")
			
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
			k = 0
			while(k < self.position[0]):
				print("_", end="")
				k +=1
			while (j < self.__size):
				print("#", end="")
				j += 1
			print()
			i += 1