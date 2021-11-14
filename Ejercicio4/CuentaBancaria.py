import datetime

class Cuenta_Bancaria:
    ID = 0
    titular= ''
    fecha_apertura= datetime.date
    num_cuenta= 0
    saldo = 0

    #Creamos un constructor sobre la cuenta
    def __init__ (self, ID, titular, fecha_apertura, num_cuenta, saldo):
        self._ID= ID
        self._titular = titular
        self._fecha_apertura = fecha_apertura.datetime
        self._num_cuenta = num_cuenta
        self._saldo = saldo


    #Creamos los metodos get y set
    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID

    def gettitular(self):
        return self._titular

    def settitular(self, titular):
        self._titular = titular

    def getfecha_apertura(self):
        return self._fecha_apertura

    def setfecha_apertura(self, fecha_apertura):
        self._fecha_apertura = fecha_apertura

    def getnum_cuenta(self):
        return self._num_cuenta

    def setnum_cuenta(self, num_cuenta):
        self._num_cuenta = num_cuenta

    def getsaldo(self):
        return int(self._saldo)

    def setsaldo(self, saldo):
        self._saldo = saldo


    #Creamos un metodo para transferir dinero
    def retirar_dinero (self, cantidad):
        if int(cantidad) > Cuenta_Bancaria.getsaldo():
            print('No se puede retirar mas dinero del que tienes')
        else:
            dinero_final= (Cuenta_Bancaria.getsaldo())- int(cantidad)
            Cuenta_Bancaria.setsaldo(dinero_final)

    def ingresar_dinero (self, cantidad):
        dinero_final= (Cuenta_Bancaria.getsaldo())+ int(cantidad)
        Cuenta_Bancaria.setsaldo(dinero_final)

    #En este metodo el primero argumento es el dinero que quiere transfereir la cuenta 1 (segundo argumento) a la cuenta 2 (tercer argumento)
    def pedir_datos():

        ID= input('Escribe el ID')
        try:
            ID = int(ID)
        except ValueError:
            print('Error de tipo')

    #La cuenta 1 es a la cuenta a la que se le tiene que transferir el dinero
    def transferir_dinero (self, cantidad,  cuenta1 ):
        if int(cantidad) > Cuenta_Bancaria.getsaldo():
            print('No se puede retirar mas dinero del que tienes')
        else:
            Cuenta_Bancaria.retirar_dinero(cantidad)
            cuenta1.ingresar_dinero(cantidad)



