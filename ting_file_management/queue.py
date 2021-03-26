class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        return None

    def search(self, index):
        return self.queue[index]
