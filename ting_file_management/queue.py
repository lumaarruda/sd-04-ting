class Queue:
    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)

    def search(self, index):
        if 0 <= index < len(self):
            return self._queue[index]
        raise IndexError(f"o index {index} não existe")
