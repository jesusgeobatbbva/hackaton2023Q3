
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
