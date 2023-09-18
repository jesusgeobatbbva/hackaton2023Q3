def depositos():
    cursor = conexion.cursor()
    id = input("\nIngrese el ID para el déposito\n >ID: " )
    idReal=validarID(id)
    
    if idReal!=False{
        monto = input("Ingrese el monto para el déposito\n >Monto: " )
        montoReal=validarMonto(monto)
        if montoReal!=False{
            sqlSaldo="SELECT Saldo FROM Client WHERE ID = " + id
            ##Ejecutar intrución SQL
            cursor.execute(sqlID)
            ##Obtener resultados
            saldoActual=cursor.fetchall()[0][0]
            ##Se regresa una lista de tuplas con los datos
            saldoNuevo=saldoActual+monto
            sqlSaldoNuevo="UPDATE Clien SET Saldo = " + saldoNuevo + "WHERE ID = " + id
            ##Ejecutar intrución SQL
            cursor.execute(sqlID)
        }
    }
    
    
    
    def validarMonto(monto):
        
        try:
            float(monto)
            return True
        except:
            print("El digito ingresado debe ser un número")
            return False
        
    def validarID(id):
        try:
            sqlID="SELECT * FROM Client WHERE ID = " + id
            ##Ejecutar intrución SQL
            cursor.execute(sqlID)
            ##Obtener resultados
            client=cursor.fetchall()
            ##Se regresa una lista de tuplas con los datos
            print("Número de cliente: " + client[0][0])
            return True
            
        except:
            print("ERROR\nEl ID no existe")
            return False
        
            