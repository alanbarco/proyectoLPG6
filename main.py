import ply.lex as lex
import ply.yacc as yacc
from lexico import tokens
from sintaxis import *
from datetime import datetime
from pytz import timezone
import lexico
import tkinter as tk

res_sintactico = []
dicc = {}
errorSemantico = False

#=========================PARTE SEMANTICO JJ=============================
def p_asignacion_let_mut_vec(p):
  '''asignacion : LET MUT ID IGUAL VEC DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'''
  global dicc
  dicc[p[3]] = p[5]

def p_vectorpush(p):
  '''
  vectorpush : ID POINT PUSH LPAREN INTTYPE RPAREN ENDCHAR
  '''
  global res_sintactico
  global dicc
  global errorSemantico
  if dicc.get(p[1],False):
    if dicc.get(p[1]) != "Vec":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES VEC")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")

#======================================================================



#==================PARTE SEMANTICO PAMELA===============================



#=======================================================================


#==================PARTE SEMANTICO ALAN===============================
def p_asignacion_let_mut_ll(p):
  '''asignacion : LET MUT ID IGUAL LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'''
  global dicc
  dicc[p[3]] = p[5]

def p_llpushfront(p):
  '''
  llpushfront : ID POINT PUSH_FRONT LPAREN INTTYPE RPAREN ENDCHAR
  '''
  global res_sintactico
  global dicc
  global errorSemantico
  if dicc.get(p[1],False):
    if dicc.get(p[1]) != "LinkedList":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES LINKEDLIST")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")

def p_llpopback(p):
  '''
  llpopback : ID POINT POP_BACK LPAREN RPAREN ENDCHAR
  '''
  global res_sintactico
  global dicc
  global errorSemantico
  if dicc.get(p[1],False):
    if dicc.get(p[1]) != "LinkedList":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES LINKEDLIST")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")
#=======================================================================

def p_error(p):
  global res_sintactico
  cadena = " "
  if p:
    cadena =  f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    res_sintactico.append(str(cadena))
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
    res_sintactico.append("Error de sintaxis Fin de Linea")
  with open('logfile.txt', 'a') as file:
      file.write(cadena + "\n")

now = datetime.now(timezone('EST')) 

parser = yacc.yacc()

#Llama las funciones del analizador, y lo que recibe el input como cadena de entrada
def validacion():
    global res_sintactico
    global errorSemantico
    entrada = input.get("1.0","end-1c")
    print(entrada)
    numeroLinea=1

    for linea in entrada.split("\n"):        
        estructura = str(parser.parse(linea))
        if estructura == "None" and not errorSemantico:
            estructura = " Linea: " + str(numeroLinea) + " Correcto"
            res_sintactico.append(estructura)
        numeroLinea+=1
        errorSemantico = False

#Llama la funcion validacion() y muestra el resultado del analizador
def sintactico():
    global res_sintactico
    validacion()
    resultado["text"] = "\n".join(res_sintactico)
    res_sintactico = []

def lex():
    entrada = input.get()
    entrada = entrada.split(" ")
    resultado["text"] = " "
    for cadena in entrada:
      lexico.lexer.input(cadena)
      tok = lexico.lexer.token()
      if tok:
        resultado["text"] += tok.type
      else:
        resultado["text"] += "Ilegal"
      resultado["text"] += "  "

root = tk.Tk()
root.title("Ventana")
root.geometry("720x800")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=1)
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side="left", fill="both", expand=1)
sb = tk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)  
sb.pack(side = "right", fill = "y")  
my_canvas.configure(yscrollcommand=sb.set)
my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion= my_canvas.bbox("all")))
second_frame = tk.Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#Elementos del GUI
titulo = tk.Label(second_frame, text="Intérprete de Rust",  bg="#93d4c5", font="Helvetica 30", fg="black")
titulo.pack(fill=tk.X)
input = tk.Text(second_frame, font="Helvetica 18",highlightthickness=2)
input.config(width=80, height=15, font=("Consolas",12),pady=20)
input.pack()
resultado = tk.Label(second_frame,  bg="#67948a", font="Helvetica 15", fg="#ffffff", text="Resultado...")
resultado.pack()


botonSemantic = tk.Button(second_frame, text = "Análisis semántico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSemantic.pack()
botonSintac = tk.Button(second_frame, text = "Análisis sintáctico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSintac.pack()
botonLex = tk.Button(second_frame, text = "Análisis léxico", padx=60,pady=10, command=lex, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonLex.pack()
root.title("bg attribute")
root['bg'] = '#f4fbf9'
root.mainloop()

''' 
while True:
  try:
    s = input('calc > ')
    with open('logfile.txt', 'a') as file:
      file.write("-------------------------\n")
      file.write("Entrada: " + "'"+s +"'" +" " + "Timestamp: " + str(now) +"\n")
    
  except EOFError:
    break
  if not s: continue
  with open('logfile.txt', 'a') as file:
      file.write("Resultado: "+ str(validaRegla(s)) + "\n")
      file.write("-------------------------\n")
'''

