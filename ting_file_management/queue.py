# import queue
import sys


class Queue:
    def __init__(self):
        self.fila = []

    def __len__(self):
        return len(self.fila)

    def enqueue(self, value):
        self.fila.append(value)

    def dequeue(self):
        if len(self.fila) == 0:
            return print("Não há elementos", file=sys.stdout)
        if self.fila:
            return self.fila.pop(0)
        return None

    def search(self, index):
        if index not in range(len(self.fila)):
            raise IndexError('index não encontrado')
        return self.fila[index]
