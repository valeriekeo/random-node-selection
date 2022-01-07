# Name: Valerie Keo
# Objective: You are given a linked list “L,” Write a program function to pick a random node from the linked list.

import random

def main():
    linkedList = LinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.insert(4)
    linkedList.insert(5)
    linkedList.insert(6)
    linkedList.printLinkedList()

    length = 0
    current = linkedList.head
    while(current):
        length += 1
        current = current.next
    print(f'\n{length}')

    # randint() is a method that generates a random number within a range, inclusive.
    iterations = random.randint(1, 6)
    selectedNode = None
    for i in range(iterations):
        if current is not None:
            current = current.next
        else:
            current = linkedList.head
        selectedNode = current
    print(selectedNode.data)

if __name__ == '__main__':
    from nodeClass import Node, LinkedList
    main()

