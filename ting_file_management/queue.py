# import queue
# from queue import Queue


class Queue:
    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        self.fila.append(value)

    def dequeue(self):
        return self.fila.pop(0)

    def search(self, index):
        if index not in range(len(self.fila)):
            raise IndexError('index não encontrado')
        return self.fila[index]
