from datetime import date
from CuentaBancaria import Cuenta_Bancaria

class Cuenta_PlazoFijo(Cuenta_Bancaria):

    def fecha_vencimiento():
        while True:
            fecha_str = input('\n Ingrese fecha "dd/mm/aaaa"...: ')
            try:
                fecha = date.strptime(fecha_str, '%d/%m/%Y')
            except ValueError:
                print("\n No ha ingresado una fecha correcta...")
            else:
                break
        return fecha
    #Creamos un metodo para transferir dinero
    def retirar_dinero (cantidad):
        fecha_vencimiento = fecha_vencimiento()

        if int(cantidad) > Cuenta_PlazoFijo.getsaldo():
            print('No se puede retirar mas dinero del que tienes')
        else:
            penalización= cantidad * 0.05
            dinero_final= (Cuenta_PlazoFijo.getsaldo())- int(cantidad)
            Cuenta_PlazoFijo.setsaldo(dinero_final)
