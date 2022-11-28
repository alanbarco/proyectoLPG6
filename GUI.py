import tkinter as tk
import main
import lexico 

root = tk.Tk()
root.title("Ventana")
root.geometry("600x600")

#Elementos del GUI
titulo = tk.Label(root, text="Intérprete de Rust",  bg="#93d4c5", font="Helvetica 30", fg="black")
titulo.pack(fill=tk.X, ipady=20)
input = tk.Entry(root, font="Helvetica 18",highlightthickness=2)
input.pack(ipadx=60,ipady=40, pady=20)
resultado = tk.Label(root,  bg="#67948a", font="Helvetica 15", fg="#ffffff", text="Resultado...")
resultado.pack(padx=60, pady=30)


#Llama las funciones del analizador, y lo que recibe el input como cadena de entrada
def validacion():
    entrada = input.get()
    return str(main.validaRegla(entrada))


#Llama la funcion validacion() y muestra el resultado del analizador
def sintactico():
    cadena = validacion()
    resultado["text"] = cadena

def lex():
    entrada = input.get()
    lexico.lexer.input(entrada)
    tok = lexico.lexer.token()
    resultado["text"] = tok

botonSintac = tk.Button(root, text = "Análisis semántico", padx=60,pady=10, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSintac.pack()
botonSintac = tk.Button(root, text = "Análisis sintáctico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSintac.pack()
botonLex = tk.Button(root, text = "Análisis léxico", padx=60,pady=10, command=lex, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonLex.pack()
root.title("bg attribute")
root['bg'] = '#f4fbf9'
root.mainloop()