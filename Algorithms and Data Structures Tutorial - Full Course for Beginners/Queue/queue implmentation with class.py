class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __repr__(self):
        return f"{''.join(str(self.items))}"


q = Queue()
q.enqueue(4)
q.enqueue(1)
print(q.size())
q.dequeue()
q.enqueue(9)
print(q)
