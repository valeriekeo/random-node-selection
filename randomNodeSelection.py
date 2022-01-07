# Name: Valerie Keo
# Objective: You are given a linked list “L,” Write a program function to pick a random node from the linked list.


def main():
    # Creating a linked list and initializing the head of the list
    linkedList = LinkedList()
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.insert(4)
    linkedList.insert(5)
    linkedList.insert(6)
    linkedList.printLinkedList()

if __name__ == '__main__':
    from nodeClass import Node, LinkedList

    main()

