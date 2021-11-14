import datetime
from CuentaBancaria import Cuenta_Bancaria
from Fecha_vencimiento import Fecha_vencimiento

class Cuenta_PlazoFijo(Cuenta_Bancaria, Fecha_vencimiento):


    #Creamos un metodo para transferir dinero
    def retirar_dinero (cantidad):
        fecha_vencimiento = Fecha_vencimiento.fecha
        fecha_hoy = datetime.date.today()
        if (fecha_vencimiento<fecha_hoy):
            if int(cantidad) > Cuenta_PlazoFijo.getsaldo():
                print('No se puede retirar mas dinero del que tienes')
            else:
                penalización= cantidad * 0.05
                dinero_final= (Cuenta_PlazoFijo.getsaldo())- int(cantidad)
                Cuenta_PlazoFijo.setsaldo(dinero_final)
