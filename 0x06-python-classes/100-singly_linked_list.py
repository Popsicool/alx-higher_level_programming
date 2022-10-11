#!/usr/bin/python3

class Node:
	def __init__(self, data, next_node=None):
		self.__data = data
		self.__next_node = next_node
	
	@property
	def data(self):
		return self.__data
	@data.setter	
	def data(self, value):
		if not (isinstance(value, int)):
			raise TypeError("data must be an integer")
		else:
			self.__data = value
	@property
	def next_node(self):
		return self.__next_node
	@next_node.setter
	def next_node(self, value):
		if (value is not None) and (isinstance(value, Node) == False):
			raise TypeError("next_node must be a Node object")
		else:
			self.__next_node = value
			
class SinglyLinkedList:
	def __init__(self):
		self.head = None
	
	def __str__(self):
	       all_node = ""
	       pos = self.head
	       while pos:
	           all_node += str(pos.data) + "\n"
	           pos = pos.next_node
	       return all_node[:-1]
	           
	def sorted_insert(self, value):
	       new = Node(value)
	       if not self.head:
	           self.head = new
	           return
	       if value < self.head.data:
	           new.next_node = self.head
	           self.head = new
	           return
	       location = self.head
	       while location.next_node and location.next_node.data < value:
	       	location = location.next_node
	       if location.next_node:
	       	new.next_node = location.next_node
	       location.next_node = new
	       
	       
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)