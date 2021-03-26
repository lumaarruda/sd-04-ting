from collections import deque


class Queue:
    def __init__(self):
        self.file_queue = deque([])

    def __len__(self):
        return len(self.file_queue)

    def enqueue(self, value):
        self.file_queue.append(value)

    def dequeue(self):
        return self.file_queue.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError

        return self.file_queue[index]
