import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import re


def es_texto_valido(valor):
    return re.fullmatch(
        r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?: +[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*",
        valor
    ) is not None


def es_entero_valido(valor):
    return re.fullmatch(r"[0-9]+", valor) is not None


def es_decimal_valido(valor):
    return re.fullmatch(r"[0-9]+(?:[.][0-9]+)?", valor) is not None


def es_entero_valido_de_10_digitos(valor):
    return re.fullmatch(r"[0-9]{10}", valor) is not None


def limpiar_campos():
    entry_nombres.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_estatura.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    var_genero.set(0)
    entry_nombres.focus_set()


def guardar_datos():
    nombres = entry_nombres.get().strip()
    apellidos = entry_apellidos.get().strip()
    edad = entry_edad.get().strip()
    estatura = entry_estatura.get().strip()
    telefono = entry_telefono.get().strip()

    if not es_texto_valido(nombres):
        messagebox.showerror(
            "Error", "Ingrese nombres válidos, solo letras y espacios."
        )
        return

    if not es_texto_valido(apellidos):
        messagebox.showerror(
            "Error", "Ingrese apellidos válidos, solo letras y espacios."
        )
        return

    if not es_entero_valido(edad):
        messagebox.showerror(
            "Error", "La edad debe ser un número entero."
        )
        return

    if not es_decimal_valido(estatura):
        messagebox.showerror(
            "Error", "Ingrese una estatura válida en centímetros. Ejemplo: 166.5"
        )
        return

    if not es_entero_valido_de_10_digitos(telefono):
        messagebox.showerror(
            "Error", "El teléfono debe tener exactamente 10 dígitos."
        )
        return

    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    else:
        messagebox.showerror("Error", "Seleccione un género.")
        return

    datos = (
        "Nombres: " + nombres
        + "\nApellidos: " + apellidos
        + "\nEdad: " + edad + " años"
        + "\nEstatura: " + estatura + " cm"
        + "\nTeléfono: " + telefono
        + "\nGénero: " + genero
    )

    ruta = Path(__file__).resolve().parent / "datos.txt"

    try:
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")
    except OSError as error:
        messagebox.showerror(
            "Error", "No se pudo guardar el archivo.\n{}".format(error)
        )
        return

    messagebox.showinfo(
        "Información",
        "Datos guardados con éxito:\n\n" + datos
    )

    limpiar_campos()


ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("350x490")

var_genero = tk.IntVar(value=0)

label_nombres = tk.Label(ventana, text="Nombres:")
label_nombres.pack(pady=(12, 0))
entry_nombres = tk.Entry(ventana, width=35)
entry_nombres.pack()

label_apellidos = tk.Label(ventana, text="Apellidos:")
label_apellidos.pack(pady=(8, 0))
entry_apellidos = tk.Entry(ventana, width=35)
entry_apellidos.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack(pady=(8, 0))
entry_edad = tk.Entry(ventana, width=35)
entry_edad.pack()

label_estatura = tk.Label(ventana, text="Estatura (cm):")
label_estatura.pack(pady=(8, 0))
entry_estatura = tk.Entry(ventana, width=35)
entry_estatura.pack()

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack(pady=(8, 0))
entry_telefono = tk.Entry(ventana, width=35)
entry_telefono.pack()

label_genero = tk.Label(ventana, text="Género:")
label_genero.pack(pady=(8, 0))

rb_hombre = tk.Radiobutton(
    ventana, text="Hombre", variable=var_genero, value=1
)
rb_hombre.pack()

rb_mujer = tk.Radiobutton(
    ventana, text="Mujer", variable=var_genero, value=2
)
rb_mujer.pack()

btn_guardar = tk.Button(
    ventana, text="Guardar", command=guardar_datos, width=20
)
btn_guardar.pack(pady=(12, 5))

btn_borrar = tk.Button(
    ventana, text="Borrar Campos", command=limpiar_campos, width=20
)
btn_borrar.pack()

entry_nombres.focus_set()
ventana.mainloop()