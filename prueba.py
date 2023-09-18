def hacer_deposito():
    cuenta_id = int(cuenta_id_entry.get())
    monto = float(deposito_entry.get())
    conn = sqlite3.connect('bancaBD.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Cuentas SET Saldo=Saldo+? WHERE idCuentas=?", (monto, cuenta_id))
    conn.commit()
    conn.close()
    consultar_saldo()
