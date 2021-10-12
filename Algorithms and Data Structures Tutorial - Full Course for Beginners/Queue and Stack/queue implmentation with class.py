class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    # Only for deque data structure

    # def popleft(self):
    #     del self.items[0]
    #     return self.items

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


q = Queue()
q.enqueue(4)
print(q)
q.enqueue(1)
print(q)
print(q.size())
q.dequeue()
print(q)
q.enqueue(9)
print(q)
q.enqueue(3)
print(q)
