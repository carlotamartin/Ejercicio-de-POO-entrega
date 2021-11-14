'''A continuación, construye una aplicación que permita crear los tres tipos de cuentas. 
El ID tiene que ser un número entero incremental, el nombre del titular puede ser inventado,
 la fecha de apertura y fecha de vencimiento deben ser aleatorias siendo la fecha de apertura
  más antigua que la fecha de vencimiento, y el número de cuenta tiene que ser un número aleatorio de 12 dígitos. 
  Cuando las cuentas estén iniciadas a un sueldo inicial de 10.000 €, 
transferir dinero de unas a otras las cantidades de 2000 €, ingresar 575 € y retirar dinero 78 €. '''

import Cuenta_PlazoFijo
import Cuenta_Vip
import CuentaBancaria
import Fecha_vencimiento

cuenta_bancaria = CuentaBancaria.Cuenta_Bancaria('56754', 'Jose MAnuel', '17/07/2020', 345678967893, 10000 )
cuenta_bancaria_vip = Cuenta_Vip.Cuenta_Vip('56754', 'Jose MAnuel', '17/07/2020', 345678967893, 10000 )
cuenta_bancaria_PlazoFIjo = Cuenta_PlazoFijo.Cuenta_PlazoFijo('56754', 'Jose MAnuel', '17/07/2020', 345678967893, 10000 )

cuenta_bancaria.transferir_dinero(2000, cuenta_bancaria_vip)
cuenta_bancaria_vip.ingresar_dinero(575)
cuenta_bancaria_PlazoFIjo.retirar_dinero(78)