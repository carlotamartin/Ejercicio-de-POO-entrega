import Nodo
class LinkedList:
    #La cabecera es un nodo que no se utiliza
    def __init__(self):
        self.cabecera = None

    #Método para añadir al principio de la lista un nodo
    def insertarPrimero (self, Nodo):
        Nodo.siguiente = self.cabecera
        self.cabecera = Nodo


    def __repr__(self):
        Nodo = self.cabecera
        Nodos = []
        while Nodo is not None:
            Nodos.append(Nodo.dato)
            Nodo = Nodo.siguiente
        Nodos.append('Nulo')
        return


    def insertarUltimo (self, Nodo):
        if self.cabecera is None:
            self.cabecera = Nodo
            return
        for current_node in self:
            pass
        current_node.next = Nodo

    def imprimir(self):
        Nodo = self.cabecera
        while Nodo is not None:
            #yield es un objeto que es capaz de retornar sus miembros uno a la vez
            yield Nodo
            Nodo = Nodo.siguiente
            print(Nodo)