import tkinter as tk
import main

root = tk.Tk()
root.title("Ventana")
root.geometry("600x500")

#Elementos del GUI
titulo = tk.Label(root, text="Intérprete de Rust",  bg="#93d4c5", font="Helvetica 30", fg="black")
titulo.pack(fill=tk.X, ipady=20)
input = tk.Entry(root, font="Helvetica 18",highlightthickness=2)
input.pack(ipadx=60,ipady=40, pady=20)
resultado = tk.Label(root,  bg="#67948a", font="Helvetica 30", fg="#ffffff", text="Resultado...")
resultado.pack(padx=60, pady=30)


#Llama las funciones del analizador, y lo que recibe el input como cadena de entrada
def validacion():
    entrada = input.get()
    return str(main.validaRegla(entrada))


#Llama la funcion validacion() y muestra el resultado del analizador
def textInput():
    cadena = validacion()
    resultado["text"] = cadena



boton = tk.Button(root, text = "Interpretar", padx=60,pady=10, command=textInput, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
boton.pack()
root.title("bg attribute")
root['bg'] = '#f4fbf9'
root.mainloop()