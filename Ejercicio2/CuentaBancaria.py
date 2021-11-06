class Cuenta_Bancaria:
    ID = 0
    titular= ''
    fecha_apertura= 0
    num_cuenta= 0
    saldo = 0

    #Creamos un constructor sobre la cuenta
    def __init__ (self, ID, titular, fecha_apertura, num_cuenta, saldo):
        self._ID= ID
        self._titular = titular
        self._fecha_apertura = fecha_apertura
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
        return self._saldo

    def setsaldo(self, saldo):
        self._saldo = saldo


    def retirar_dinero (cantidad):
        self._saldo = (saldo-cantidad)
