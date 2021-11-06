'''
Ejercicio 1
Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python.
Respuesta
En primer lugar, se listan las propiedades o atributos de un libro:
Título, Autor, Editor, Número de páginas,Año
A continuación, se listan los métodos que permiten gestionar estas propiedades:
1. Modificar cada uno de los atributos anteriores.
2. Acceder a los atributos.
3. Crear un nuevo objeto libro a través de uno o varios constructores.
Un constructor por defecto va a inicializar las variables, otro tomará todos los valores. A continuación se implementan algunos métodos.
'''

class libro:
    titulo = ''
    autor = ''
    editor = ''
    num_paginas = 0
    año = 0

    #Creamos un constructor con todos los atributos principales de un libro
    def __init__ (self, titulo, autor, genero, num_paginas, año):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._num_paginas = num_paginas
        self._año = año

    #Creamos el metodos get y set para cada atributo
    def gettitulo(self):
        return self._titulo

    def gettautor(self):
        return self._autor

    def gettgenero(self):
        return self._genero

    def gettnum_paginas(self):
        return self._num_paginas

    def gettaño(self):
        return self._año

    def settitulo(self, titulo):
        self._titulo = titulo

    def setautor(self, autor):
        self._autor = autor

    def setgenero(self, genero):
        self._genero = genero

    def setnum_paginas(self, num_paginas):
        self._num_paginas = num_paginas

    def setaño(self, año):
        self._año = año


