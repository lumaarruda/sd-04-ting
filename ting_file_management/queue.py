class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        return self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return None
        else:
            self.queue.pop(0)

    def search(self, index):
        return self.queue[index]:
