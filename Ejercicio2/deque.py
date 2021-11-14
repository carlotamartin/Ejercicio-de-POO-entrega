from collections import deque

class Linked_list(deque):
    def __init__(self, deque):
        self.deque = deque

    def insertarultimo(self, elemento):
        return deque.append(elemento)

    def insertarprimero (self, elemento):
        return deque.appendleft(elemento)

    def eliminarprimero(self):
        return deque.popleft()

    def eliminarultimo (self):
        return deque.pop()

    def eliminar (self, elemento):
        return deque.remove(elemento)

    def esta_vacio():
        resultado = False
        if deque.__len__ == 0:
            resultado = True
        return resultado

    def imprimir_izq_a_drch ():
        return print(deque)

    def imprimir_drch_a_izq ():
        deque.reverse()
        return print(deque)

    def eliminar_todo ():
        return deque.clear()


