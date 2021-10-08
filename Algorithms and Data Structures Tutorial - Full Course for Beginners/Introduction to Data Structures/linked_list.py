#  Singly linked list

"""
each element of the list, contains information(reference) about the net element in the list
"""


class Node:  # class Node stores a single node of a linked list
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"Node data: {self.data}"


class LinkedList:

    # Singly linked list

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None  # checks if the list is empty or not

    def size(self):  # checks the number of the nodes in the linked list. It takes -> O(n) -> time complexity
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):  # add new node at the head (Zero index) of the linked list. Takes constant time complexity - The Best case
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node that matches the searched key
        Takes O(n) -> linear time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """"
        insert a new Node with data at index position
        Insertion takes O(1) time complexity, but finding the node at the insertion point takes O(n) time.
        Overall it takes O(n) -> linear time
        """
        if index == 0:
            self.add(data)
            return

        elif index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = new_node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self, key):
        """
        Removes Node with the data, which matches the key
        Returns the Node ot None if key doesn't exist
        Takes O(n) time, because in the worst case, we should traverse through the entire list

        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        returns a string representation of the list
        Takes O(n) time -> Linear time

        """
        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        return f"{'-> '.join(map(str, nodes))}"


l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
# print(l.size())
# print(l)
print(l.search(1))
# l.insert(4, 2) -> method not working -> throws error
l.remove(2)
print(l)

"""
Double linked list is list, which stores information about the next and the previous element in the list
"""
