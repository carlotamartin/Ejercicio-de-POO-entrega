import datetime 
from CuentaBancaria import Cuenta_Bancaria

class Cuenta_PlazoFijo(Cuenta_Bancaria):

    #Creamos un metodo para transferir dinero
    def retirar_dinero (cantidad):
        fecha_vencimiento = Cuenta_Bancaria.getfecha_apertura()
        fecha_hoy = datetime.date.today()
        if (fecha_vencimiento<fecha_hoy):
            if int(cantidad) > Cuenta_PlazoFijo.getsaldo():
                print('No se puede retirar mas dinero del que tienes')
            else:
                penalización= cantidad * 0.05
                dinero_final= (Cuenta_PlazoFijo.getsaldo())- int(cantidad)
                Cuenta_PlazoFijo.setsaldo(dinero_final)
