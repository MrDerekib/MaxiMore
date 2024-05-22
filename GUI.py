import tkinter as tk

def accion_boton():
    print("Botón presionado")

def seleccionar_opcion(evento):
    print("Opción seleccionada:", lista_desplegable.get())


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("MáxiMore")

# Configurar el grid
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Crear un frame principal para contener los widgets
frame_principal = tk.Frame(ventana)
frame_principal.grid(sticky='nsew')

# Configurar el grid del frame principal
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)

# Crear un TextBox dentro del frame principal
texto = tk.Entry(frame_principal, width=50)
texto.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

# Crear varios botones dentro del frame principal
boton1 = tk.Button(frame_principal, text="Botón 1", command=accion_boton)
boton1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

boton2 = tk.Button(frame_principal, text="Botón 2", command=accion_boton)
boton2.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

boton3 = tk.Button(frame_principal, text="Botón 3", command=accion_boton)
boton3.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

etiqueta = tk.Label(frame_principal, text="Generar listado")
etiqueta.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

# Crear una lista desplegable dentro del frame principal
opciones = ["TMB", "Linea9", "T-Mobilitat", "Renfe", "FGC", "Boixeres"]
lista_desplegable = tk.StringVar(frame_principal)
lista_desplegable.set(opciones[0]) # opción por defecto
menu_desplegable = tk.OptionMenu(frame_principal, lista_desplegable, *opciones, command=seleccionar_opcion)
menu_desplegable.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

boton4 = tk.Button(frame_principal, text="Generar", command=accion_boton)
boton4.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

# Ajustar el tamaño de los widgets al tamaño del frame
frame_principal.grid_columnconfigure(0, weight=1)

# Iniciar el bucle de eventos
ventana.mainloop()
