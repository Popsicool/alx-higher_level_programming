#!/usr/bin/python3
""" Declare class Node"""


class Node:
    """ initialze node"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    """ retrive data property"""
    @property
    def data(self):
        return self.__data
    """ set data"""
    @data.setter
    def data(self, value):
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    """ retrive property next_node"""
    @property
    def next_node(self):
        return self.__next_node
    """ setter next node"""
    @next_node.setter
    def next_node(self, value):
        if (value is not None) and (isinstance(value, Node) is False):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" declare class SinglyLinkedList"""


class SinglyLinkedList:
    """ initialize class"""
    def __init__(self):
        self.head = None

    """ print all"""
    def __str__(self):
        all_node = ""
        pos = self.head
        while pos:
            all_node += str(pos.data) + "\n"
            pos = pos.next_node
        return all_node[:-1]
    """ sorted_insert method"""
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
