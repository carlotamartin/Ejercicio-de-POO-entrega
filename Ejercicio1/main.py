from libro import libro

#Creamos un nuevo libro
libro_historia_de_una_escalera = libro('Historia de una escalera', 'Antonio Buero Vallejo', 'Drama', 170,  1947 )

print ("Su nombre es '"+ libro_historia_de_una_escalera.gettitulo()+"'")

#Cambiamos el año de publicación
libro_historia_de_una_escalera.setaño(1948)

print('La fecha de publicacion es: '+ str(libro_historia_de_una_escalera.gettaño()))