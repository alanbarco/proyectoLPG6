from tkinter.ttk import Scrollbar
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
def asignacionConstCheck(p_clave):
  global res_sintactico , errorSemantico, dicc
  print(dicc)
  if dicc.get(p_clave,False):
    res_sintactico.append("ERROR SEMÁNTICO: REASIGNACIÓN DE CONSTANTE")
    errorSemantico = True
    return False
  return True

def p_asignacion_let_mut_vec(p):
  '''asignacion : LET MUT ID IGUAL VEC DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'''
  global dicc
  if asignacionConstCheck(p[3]):
    dicc[p[3]] = {"asig":p[2], "tipo": p[5]}

def p_asignacion_const_int(p):
  '''
  asignacion : CONST ID COLON intsize IGUAL INTTYPE ENDCHAR
  | CONST ID COLON intsize IGUAL NINTTYPE ENDCHAR
  '''
  global dicc

  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "valor": "int"}

def p_asignacion_const_uint(p):
  'asignacion : CONST ID COLON uintsize IGUAL INTTYPE ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "uint"}
  
def p_asignacion_const_float(p):
  'asignacion : CONST ID COLON floatsize IGUAL FLOATTYPE ENDCHAR'
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "float"}

def p_asignacion_const_str(p):
  'asignacion : CONST ID COLON strsize IGUAL IDSTRING ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "str"}

def p_asignacion_const_string(p):
  'asignacion : CONST ID COLON STRING IGUAL STRING DOSDOBLEPUNTOS FROM LPAREN IDSTRING RPAREN ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "string"}

def p_asignacion_const_string2(p):
  'asignacion : CONST ID COLON STRING IGUAL IDSTRING ENDCHAR'
  global dicc  
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "string"}

def p_asignacion_const_bool(p):
  'asignacion : CONST ID COLON BOOL IGUAL boolean ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "bool"}

def p_asignacion_const_char(p):
  'asignacion : CONST ID COLON CHAR IGUAL IDCHAR ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "char"}

def p_vectorpush(p):
  '''
  vectorpush : ID POINT PUSH LPAREN INTTYPE RPAREN ENDCHAR
  '''
  global res_sintactico, dicc, errorSemantico

  if dicc.get(p[1],False):
    if dicc.get(p[1]).get("tipo") != "Vec":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES VEC")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")



#======================================================================



#==================PARTE SEMANTICO PAMELA===============================

#Asignacion con let mut
def p_asignacion_let_mut(p):
  '''asignacion : LET MUT ID IGUAL valor ENDCHAR
  | LET MUT ID IGUAL estructuras ENDCHAR'''
  global dicc
  if asignacionConstCheck(p[3]):
    dicc[p[3]] = p[2]
  

#Asignacion con let
def p_asignacion_let(p):
  '''asignacion : LET ID IGUAL valor ENDCHAR'''
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":"let", "tipo": p[4]}
#=======================================================================


#==================PARTE SEMANTICO ALAN===============================

#SUMA VARIABLES

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

parser = yacc.yacc()

#Llama las funciones del analizador, y lo que recibe el input como cadena de entrada
def validacion():
    global res_sintactico, errorSemantico
    entrada = input.get("1.0","end-1c")
    numeroLinea=1
    with open('logfile.txt', 'a') as file:
      file.write(entrada + "\n") 

    for linea in entrada.split("\n"):  
        estructura = str(parser.parse(linea))
        if estructura == "None" and not errorSemantico:
            estructura = " Linea: " + str(numeroLinea) + " Correcto"
            res_sintactico.append(estructura)
        numeroLinea+=1
        errorSemantico = False

#Llama la funcion validacion() y muestra el resultado del analizador
def sintactico():
    now = datetime.now(timezone('EST')) 
    global res_sintactico
    file = open('logfile.txt', 'a')
    file.write("-----Análisis Sintáctico/Semántico - Timestamp: " + str(now) +"\nEntrada: ")   
    validacion()
    resultado["text"] = "\n".join(res_sintactico)
    file.write("\n".join(res_sintactico))
    res_sintactico = []
    file.close()

def lex():
    now = datetime.now(timezone('EST')) 
    file = open('logfile.txt', 'a')
    file.write("----------Análisis Léxico - Timestamp: "+  str(now) + "\n Entrada: ")
    entrada = input.get("1.0","end-1c")
    file.write(entrada)
    entrada = entrada.split("\n")

    file.write("Resultado:  ")

    resultado["text"] = " "
    line_number = 1
    for cadena in entrada:
      lexico.lexer.input(cadena)
      tok = lexico.lexer.token()
      if tok:
        if line_number != tok.lineno:
          file.write("\n")
          line_number = tok.lineno
        file.write(tok.type)
        resultado["text"] += tok.type
      else:
        file.write("Ilegal")
        resultado["text"] += "Ilegal"
      resultado["text"] += "  "
      file.write(" ")
    file.w

def limpiar():
  global dicc
  dicc = {}

root = tk.Tk()
root.title("Ventana")
root.geometry("800x800")

#Elementos del GUI
titulo = tk.Label(root, text="Intérprete de Rust",  bg="#93d4c5", font="Helvetica 30", fg="black")
titulo.pack(fill=tk.X, ipady=20)
input = tk.Text(root, font="Helvetica 18",highlightthickness=2)
input.config(width=55, height=15, font=("Consolas",12),pady=20)
input.pack(ipadx=10,ipady=10, pady=20)
resultado = tk.Label(root,  bg="#67948a", font="Helvetica 15", fg="#ffffff", text="Resultado...")
resultado.pack(padx=60, pady=30)

botonSemantic = tk.Button(root, text = "Análisis semántico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSemantic.pack()
botonSintac = tk.Button(root, text = "Análisis sintáctico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSintac.pack()
botonLex = tk.Button(root, text = "Análisis léxico", padx=60,pady=10, command=lex, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonLex.pack()
botonDicc = tk.Button(root, text = "Limpiar Variables", padx=60,pady=10, command=limpiar, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") 
botonDicc.pack()
root.title("bg attribute")
root['bg'] = '#f4fbf9'
root.mainloop()