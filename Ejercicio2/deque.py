from collections import deque

class Linked_list(deque):
    def __init__(self):
        self.cabecera = None

    def insertarultimo(self, elemento):
        deque.append(elemento)
    
    def insertarprimero (self, elemento):
        deque.appendleft(elemento)
    def eliminarprimero(self, elemento):
        deque.popleft(elemento)
    def eliminar (self, elemento):
        deque.