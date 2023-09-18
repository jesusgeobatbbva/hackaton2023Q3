import tkinter as tk
from tkinter import ttk
import sqlite3

# Función para consultar el saldo de una cuenta
def consultar_saldo():
    cuenta_id = int(cuenta_id_entry.get())
    cuenta_id_entry_deposito.delete(0, tk.END)
    cuenta_id_entry_deposito.insert(0, cuenta_id)
    conn = sqlite3.connect('banco (1).db')
    cursor = conn.cursor()
    cursor.execute("SELECT Saldo FROM Cuentas WHERE idCuentas=?", (cuenta_id,))
    saldo = cursor.fetchone()
    conn.close()
    if saldo:
        saldo_label.config(text=f"Saldo: {saldo[0]}")
    else:
        saldo_label.config(text="Cuenta no encontrada")

# Función para hacer un depósito
def hacer_deposito():
    cuenta_id = int(cuenta_id_entry.get())
    monto = float(deposito_entry.get())
    conn = sqlite3.connect('bancaBD.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Cuentas SET Saldo=Saldo+? WHERE idCuentas=?", (monto, cuenta_id))
    conn.commit()
    conn.close()
    consultar_saldo()

# Función para hacer un retiro
def hacer_retiro():
    cuenta_id = int(cuenta_id_entry.get())
    monto = float(retiro_entry.get())
    conn = sqlite3.connect('bancaBD.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Saldo FROM Cuentas WHERE idCuentas=?", (cuenta_id,))
    saldo = cursor.fetchone()
    if saldo and saldo[0] >= monto:
        cursor.execute("UPDATE Cuentas SET Saldo=Saldo-? WHERE idCuentas=?", (monto, cuenta_id))
        conn.commit()
        conn.close()
        consultar_saldo()
    else:
        conn.close()
        saldo_label.config(text="Saldo insuficiente")

# Función para transferir fondos entre dos cuentas
def hacer_transferencia():
    cuenta_origen_id = int(cuenta_origen_entry.get())
    cuenta_destino_id = int(cuenta_destino_entry.get())
    monto = float(transferencia_entry.get())
    conn = sqlite3.connect('bancaBD.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Saldo FROM Cuentas WHERE idCuentas=?", (cuenta_origen_id,))
    saldo_origen = cursor.fetchone()
    cursor.execute("SELECT Saldo FROM Cuentas WHERE idCuentas=?", (cuenta_destino_id,))
    saldo_destino = cursor.fetchone()
    if saldo_origen and saldo_destino and saldo_origen[0] >= monto:
        cursor.execute("UPDATE Cuentas SET Saldo=Saldo-? WHERE idCuentas=?", (monto, cuenta_origen_id))
        cursor.execute("UPDATE Cuentas SET Saldo=Saldo+? WHERE idCuentas=?", (monto, cuenta_destino_id))
        conn.commit()
        conn.close()
        consultar_saldo()
    else:
        conn.close()
        saldo_label.config(text="Saldo insuficiente o cuentas no encontradas")

# Función para ver el historial de transacciones de una cuenta
def ver_historial():
    cuenta_id = int(historial_cuenta_id_entry.get())
    conn = sqlite3.connect('bancaBD.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Transacciones WHERE idCuentas=?", (cuenta_id,))
    historial = cursor.fetchall()
    conn.close()
    historial_text.config(state=tk.NORMAL)
    historial_text.delete(1.0, tk.END)
    if historial:
        for transaccion in historial:
            historial_text.insert(tk.END, f"Tipo: {transaccion[2]}, Monto: {transaccion[3]}, Fecha: {transaccion[4]}\n")
    else:
        historial_text.insert(tk.END, "No hay transacciones para esta cuenta\n")
    historial_text.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador Bancario")

# Crear pestañas
tab_control = ttk.Notebook(root)
tab_control.pack()

tab_saldo = ttk.Frame(tab_control)
tab_deposito = ttk.Frame(tab_control)
tab_retiro = ttk.Frame(tab_control)
tab_transferencia = ttk.Frame(tab_control)
tab_historial = ttk.Frame(tab_control)

tab_control.add(tab_saldo, text="Consultar Saldo")
tab_control.add(tab_deposito, text="Hacer Depósito")
tab_control.add(tab_retiro, text="Hacer Retiro")
tab_control.add(tab_transferencia, text="Hacer Transferencia")
tab_control.add(tab_historial, text="Historial de Transacciones")

cuenta_actual = tk.StringVar()

# Interfaz para consultar saldo
tk.Label(tab_saldo, text="ID de la Cuenta:").grid(row=0, column=0)
cuenta_id_entry = tk.Entry(tab_saldo)
cuenta_id_entry.grid(row=0, column=1)
saldo_button = tk.Button(tab_saldo, text="Consultar Saldo", command=consultar_saldo)
saldo_button.grid(row=0, column=2)
saldo_label = tk.Label(tab_saldo, text="")
saldo_label.grid(row=1, column=0, columnspan=3)

# Interfaz para hacer un depósito
tk.Label(tab_deposito, text="ID de la Cuenta:").grid(row=0, column=0)
cuenta_id_entry_deposito = tk.Entry(tab_deposito)

tk.Label(tab_deposito, text="Monto del Depósito en Pesos $:").grid(row=1, column=0)
deposito_entry = tk.Entry(tab_deposito)
deposito_entry.grid(row=1, column=1)
deposito_button = tk.Button(tab_deposito, text="Hacer Depósito", command=hacer_deposito)
deposito_button.grid(row=2, column=1)

# Interfaz para hacer un retiro
tk.Label(tab_retiro, text="ID de la Cuenta:").grid(row=0, column=0)
tk.Label(tab_retiro, text="Monto del Retiro:").grid(row=1, column=0)
retiro_entry = tk.Entry(tab_retiro)
retiro_entry.grid(row=0, column=1)
retiro_button = tk.Button(tab_retiro, text="Hacer Retiro", command=hacer_retiro)
retiro_button.grid(row=1, column=1)

# Interfaz para hacer una transferencia
tk.Label(tab_transferencia, text="Cuenta de Origen:").grid(row=0, column=0)
tk.Label(tab_transferencia, text="Cuenta de Destino:").grid(row=1, column=0)
tk.Label(tab_transferencia, text="Monto de la Transferencia:").grid(row=2, column=0)
cuenta_origen_entry = tk.Entry(tab_transferencia)
cuenta_origen_entry.grid(row=0, column=1)
cuenta_destino_entry = tk.Entry(tab_transferencia)
cuenta_destino_entry.grid(row=1, column=1)
transferencia_entry = tk.Entry(tab_transferencia)
transferencia_entry.grid(row=2, column=1)
transferencia_button = tk.Button(tab_transferencia, text="Hacer Transferencia", command=hacer_transferencia)
transferencia_button.grid(row=3, column=0, columnspan=2)

# Interfaz para ver el historial de transacciones
tk.Label(tab_historial, text="ID de la Cuenta:").grid(row=0, column=0)
historial_cuenta_id_entry = tk.Entry(tab_historial)
historial_cuenta_id_entry.grid(row=0, column=1)
historial_button = tk.Button(tab_historial, text="Ver Historial", command=ver_historial)
historial_button.grid(row=0, column=2)
historial_text = tk.Text(tab_historial, height=10, width=50, state=tk.DISABLED)
historial_text.grid(row=1, column=0, columnspan=3)

root.mainloop()
