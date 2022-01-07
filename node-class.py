# Name: Valerie Keo
# Objective: Create a node object

class Node:
    # To create a constructor for the node class, use the __init__ function, which assigns values to
    # object properties
    # The self parameter refers to the current instance of the class, and is used to access variables that
    # belongs to the class
    def __init__(self, data, next):
        self.data = data
