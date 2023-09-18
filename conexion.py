import mysql.connector
conexion = mysql.connector.connect(user="root", password="123",
                                    host='localhost',
                                    database='banco2',
                                    port='3306')

def consulta():
curs = conexion.cursor()

#funcion 1 : Implementar una función para consultar el saldo de una cuenta.
#pruebas insercion datos
#print("ingrese su numero de cuenta")

#En esta linea de abajo comentada se permite ingresar datos a la base de datos 
#curs.execute("insert into cuenta values(15,'Roberto',780)",)
#id = input("Ingrese su id")
curs.execute('select saldo from cuenta where id=15')
#ingresar muchos datos al mismo tiempo
#trae los resultados 
result = curs.fetchall()
print("Estimado usuario, el saldo de su cuenta es: ")
print(result)
conexion.commit()
conexion.close()
