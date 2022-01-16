# random-node-selection
You are given a linked list “L,” Write a program function to pick a random node from the linked list.

Solution:
* Assume it is a singly-linked list. Find the length of the list. Generate a random number within the range of the linked list, and select the node with that generated index.
* Unwritten alternative: Assume it is a singly-linked list. Generate a random number, and select the node with that generated index. If you reach the end of the list, return to the beginning.
* Problem with alternative: Generated number could be excessively large. Does not increase randomness over the first solution.
