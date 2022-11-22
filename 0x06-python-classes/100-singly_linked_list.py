#!/usr/bin/python3

"""
-Defines a class Node that defines a node of a singly linked list.
-Defines a class SinglyLinkedList.
"""
class Node():
    """Defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Instantiates a node.
        Attr:
            data: node data(int).
            next_node: next node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__value = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None or value.__class__.__name__ != "Node":
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList():
    """Defines a singly linkedlist."""
    def __init__(self):
        """Instantiates a linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Adds a node to the list."""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None
                    and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Prints the list."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(temp.value)
            temp = temp.next_node
        return ("\n".join(values))
