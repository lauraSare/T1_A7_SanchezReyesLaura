'''
Created on 14 mar. 2024

@author: laura

'''
from tkinter import *
import tkinter as tk 
from tkinter import messagebox as mg
from LogicaCalculadora import Calculadora

calculadora = Calculadora()
 
ventana_inicio = Tk()
ventana_inicio.title("----GUI con PYTHON----")
ventana_inicio.geometry("450x500")

numeros = StringVar()
caja_operaciones = Entry(ventana_inicio, bg="white", 
                        fg="black", font=("roboto", 20, "bold"),
                        width=30, justify=tk.RIGHT, textvariable=numeros)
caja_operaciones.grid(row=0, columnspan=4)

def mostrarNumero(num):
    numeros.set(numeros.get() + num)

def indicarSuma():
    calculadora.indicarOperacion_Numero(numeros.get(), "+")
    numeros.set("")

def indicarResta():
    calculadora.indicarOperacion_Numero(numeros.get(), "-")
    numeros.set("")

def indicarMultiplicacion():
    calculadora.indicarOperacion_Numero(numeros.get(), "*")
    numeros.set("")

def indicarDivision():
    calculadora.indicarOperacion_Numero(numeros.get(), "/")
    numeros.set("")

def obtenerResultado():
    calculadora.indicarSegundoNumero(numeros.get())
    resultado = calculadora.realizarOperacion()
    if isinstance(resultado, str):
        mg.showerror("Error", resultado)
    else:
        numeros.set(resultado)


for i in range(1, 10):
    btn = Button(ventana_inicio, text=str(i), width=5, height=5, bg="gray", fg="black",
                 command=lambda i=i: mostrarNumero(str(i)))
    btn.grid(row=(i - 1) // 3 + 2, column=(i - 1) % 3)

btn_cero = Button(ventana_inicio, text="0", width=17, height=5, bg="gray", fg="black",
                  command=lambda: mostrarNumero("0"))
btn_cero.grid(row=5, column=0, columnspan=2)


btn_suma = Button(ventana_inicio, text="+", width=5, height=5, bg="gray", fg="black", 
                  command=indicarSuma)
btn_suma.grid(row=2, column=3)

btn_resta = Button(ventana_inicio, text="-", width=5, height=5, bg="gray", fg="black", 
                  command=indicarResta)
btn_resta.grid(row=3, column=3)

btn_multiplicacion = Button(ventana_inicio, text="*", width=5, height=5, bg="gray", fg="black", 
                  command=indicarMultiplicacion)
btn_multiplicacion.grid(row=4, column=3)

btn_division = Button(ventana_inicio, text="/", width=5, height=5, bg="gray", fg="black", 
                  command=indicarDivision)
btn_division.grid(row=5, column=3)

btn_igual = Button(ventana_inicio, text="=", width=5, height=5, bg="gray", fg="black",
                   command=obtenerResultado)
btn_igual.grid(row=5, column=2)

ventana_inicio.mainloop()
