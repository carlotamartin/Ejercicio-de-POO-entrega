from CuentaBancaria import Cuenta_Bancaria


class Cuenta_Vip(Cuenta_Bancaria):

    def pedirsaldomin():
        saldo_min = int(input('Escribe el saldo minimo: '))
        return saldo_min

    def comprobacion_saldo():
        supera_minimo = False
        saldo_min = pedirsaldomin()
        if (Cuenta_Bancaria.getsaldo<saldo_min):
            return print('No se puede tenemos menos dinero que '+ saldo_min)
