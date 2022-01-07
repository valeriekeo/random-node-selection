# Name: Valerie Keo
# Objective: Create a node object

# Node of a singly linked list
class Node:
    # To create a constructor for the node class, use the __init__ function, which assigns values to
    # object properties
    # The self parameter refers to the current instance of the class, and is used to access variables that
    # belongs to the class
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        # Checks if there is at least one node in the list, and creates it if not
        if (self.head):
            current = self.head
            while(current.next):
                current = current.next
            # At last node in the list, insert node
            current.next = newNode
        else:
            self.head = newNode

    def printLinkedList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
