class Queue:
    FIRST_ELEMENT = 0

    def __init__(self):
        self._queue = list()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(self.FIRST_ELEMENT)
        return None

    def search(self, index):
        if 0 <= index < len(self):
            return self._queue[index]
        raise IndexError('error')
        
