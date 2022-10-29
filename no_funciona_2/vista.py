from tkinter import Tk
from tkinter import StringVar
from tkinter import Button
from tkinter import Label
from tkinter import ttk
from tkinter import Entry
from tkinter import W
from tkcalendar import Calendar
from tkcalendar import DateEntry
import locale
import modelo
import datetime
import os
from datetime import date
from datetime import timedelta


os.system("cls")


# *******************************************************************
# VISTA VISTA VISTA VISTA VISTA VISTA VISTA VISTA VISTA VISTA VISTA *
# *******************************************************************
root = Tk()

var_fecha_inicio = StringVar()
var_fecha_fin = StringVar()
var_nombre = StringVar()
var_direccion = StringVar()
var_telefono = StringVar()
var_mail = StringVar()
variable_autos = StringVar()
sel_fecha_inicio = StringVar()
sel_fecha_fin = StringVar()
locale.setlocale(locale.LC_TIME, "es_ES")


# ****************************************************************
# ventana principal
# ****************************************************************
root.title("Alquiler de Autos - Reservas")
root.geometry("860x600")

boton_reservar = Button(
    root,
    text="Reservar",
    command=lambda: modelo.f_boton_reservar(
        tree,
        fecha_inicio,
        fecha_fin,
        variable_autos,
        e_telefono,
        e_mail,
        e_nombre,
        e_direccion,
        cal,
    ),
)
boton_reservar.place(x=10, y=565, width=100, height=25)

boton_baja = Button(root, text="Baja", command=lambda: modelo.f_boton_baja(tree))
boton_baja.place(x=120, y=565, width=100, height=25)

boton_modificar = Button(
    root,
    text="Modificar",
    command=lambda: modelo.f_boton_modificar(
        tree,
        variable_autos,
        e_telefono,
        e_mail,
        e_nombre,
        e_direccion,
        fecha_inicio,
        fecha_fin,
    ),
)
boton_modificar.place(x=230, y=565, width=100, height=25)

boton_salir = Button(root, text="Salir", command=lambda: modelo.f_boton_salir(root))
boton_salir.place(x=490, y=565, width=100, height=25)


variable_autos = ttk.Combobox(state="readonly", values=modelo.lista_de_autos)
variable_autos.place(x=30, y=250, height=30)
variable_autos.current(0)


# ****************************************************************
# calendario
# ****************************************************************
now = datetime.datetime.now()
now = str(now).split(" ")
now = now[0].split("-")
cal = Calendar(
    root,
    selectmode="day",
    year=int(now[0]),
    month=int(now[1]),
    day=int(now[2]),
    locale="es_ES",
    state="disabled",
)

cal.place(x=30, y=55)

modelo.inicializar_calendario(cal)


# ****************************************************************
# Campo entrada fecha inicio y fin
# ****************************************************************
fecha_inicio = DateEntry(
    root,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    locale="es_ES",
    textvariable=sel_fecha_inicio,
)


fecha_fin = DateEntry(
    root,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    locale="es_ES",
    textvariable=sel_fecha_fin,
)
fecha_fin.place(x=160, y=20, width=100, height=25)


fecha_inicio.place(x=50, y=20, width=100, height=25)

sel_fecha_inicio.trace(
    "w",
    lambda evento, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, cal=cal, boton_reservar=boton_reservar: modelo.fecha_inicio_seleccionada(
        fecha_inicio,
        fecha_fin,
        cal,
        boton_reservar,
    ),
)
fecha_inicio.delete(0, "end")

sel_fecha_fin.trace(
    "w",
    lambda evento, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, cal=cal, boton_reservar=boton_reservar, variable_autos=variable_autos: modelo.fecha_fin_seleccionada(
        fecha_inicio,
        fecha_fin,
        cal,
        boton_reservar,
        variable_autos,
    ),
)
fecha_fin.delete(0, "end")


# ****************************************************************
# Datos del cliente
# ****************************************************************
label_nombre = Label(root, text="Nombre:")
label_nombre.place(x=10, y=385)

label_telefono = Label(root, text="Telefono:")
label_telefono.place(x=10, y=420)

label_direccion = Label(root, text="Direccion:")
label_direccion.place(x=10, y=455)

label_mail = Label(root, text="Mail:")
label_mail.place(x=10, y=490)

e_nombre = Entry(root, textvariable=var_nombre)
e_nombre.place(x=120, y=385, width=710, height=25)

e_telefono = Entry(root, textvariable=var_telefono)
e_telefono.place(x=120, y=420, width=710, height=25)

e_direccion = Entry(root, textvariable=var_direccion)
e_direccion.place(x=120, y=455, width=710, height=25)

e_mail = Entry(root, textvariable=var_mail)
e_mail.place(x=120, y=490, width=710, height=25)

# ****************************************************************
# Treeview - lista de reservas
# ****************************************************************
tree_frame = ttk.Frame(root)
tree_frame.config(height=10)
tree_frame.pack()

tree = ttk.Treeview(root, show="headings")
tree["columns"] = ("col1", "col2", "col3", "col4")

tree.heading("col1", text="ID")
tree.heading("col2", text="Vehiculo")
tree.heading("col3", text="Desde")
tree.heading("col4", text="Hasta")

tree.column("col1", width=10, minwidth=10, anchor=W)
tree.column("col2", width=120, minwidth=80, anchor=W)
tree.column("col3", width=20, minwidth=20, anchor=W)
tree.column("col4", width=20, minwidth=20, anchor=W)

tree.place(x=330, y=20, width=500, height=340)

#       ----------Barra de dezplazamiento-----------------
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.place(x=330 + 500 + 2, y=20, height=340)

modelo.inicializar_treview(tree)

tree.bind(
    "<Double-1>",
    lambda evento, tree=tree, e_nombre=e_nombre, e_telefono=e_telefono, e_direccion=e_direccion, e_mail=e_mail, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, variable_autos=variable_autos, boton_reservar=boton_reservar: modelo.bind_accion(
        tree,
        e_nombre,
        e_telefono,
        e_direccion,
        e_mail,
        fecha_inicio,
        fecha_fin,
        variable_autos,
        boton_reservar,
    ),
)  # accion al seleccionar un tree


root.mainloop()
modelo.con.close()
