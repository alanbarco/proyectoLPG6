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
    dicc[p[3]] = {"asig":p[2], "tipo": p[5], "valor": "["}

def p_asignacion_const_int(p):
  '''
  asignacion : CONST ID COLON intsize IGUAL INTTYPE ENDCHAR
  | CONST ID COLON intsize IGUAL NINTTYPE ENDCHAR
  '''
  global dicc

  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": p[4], "valor" : p[6]}

def p_asignacion_const_uint(p):
  'asignacion : CONST ID COLON uintsize IGUAL INTTYPE ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": p[4] , "valor": p[6]}
  
def p_asignacion_const_float(p):
  'asignacion : CONST ID COLON floatsize IGUAL FLOATTYPE ENDCHAR'
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": p[4] , "valor": p[6]}

def p_asignacion_const_str(p):
  'asignacion : CONST ID COLON strsize IGUAL IDSTRING ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "str", "valor": p[6]}

def p_asignacion_const_string(p):
  'asignacion : CONST ID COLON STRING IGUAL STRING DOSDOBLEPUNTOS FROM LPAREN IDSTRING RPAREN ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "string", "valor": p[6]}

def p_asignacion_const_string2(p):
  'asignacion : CONST ID COLON STRING IGUAL IDSTRING ENDCHAR'
  global dicc  
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "string", "valor": p[6]}

def p_asignacion_const_bool(p):
  'asignacion : CONST ID COLON BOOL IGUAL boolean ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "bool" , "valor": p[6]}

def p_asignacion_const_char(p):
  'asignacion : CONST ID COLON CHAR IGUAL IDCHAR ENDCHAR'
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":p[1], "tipo": "char", "valor": p[6]}

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
    dicc[p[3]] = {"asig":"mut", "tipo": "nd","valor": p[5]}
  
#Asignacion con let
def p_asignacion_let_int(p):
  '''asignacion : LET ID IGUAL valor ENDCHAR'''
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[2]] = {"asig":"let", "tipo": "i32" , "valor" : p[4]}

#=======================================================================


#==================PARTE SEMANTICO ALAN===============================
def p_asignacion_let_mut_ll(p):
  '''asignacion : LET MUT ID IGUAL LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'''
  global dicc
  if asignacionConstCheck(p[2]):
    dicc[p[3]] = {"asig":"mut", "tipo": p[5]}

def p_llpushfront(p):
  '''
  llpushfront : ID POINT PUSH_FRONT LPAREN INTTYPE RPAREN ENDCHAR
  '''
  global res_sintactico , dicc, errorSemantico
  if dicc.get(p[1],False):
    if dicc.get(p[1]).get("tipo") != "LinkedList":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES LINKEDLIST")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")

def p_llpopback(p):
  '''
  llpopback : ID POINT POP_BACK LPAREN RPAREN ENDCHAR
  '''
  global res_sintactico , dicc, errorSemantico
  if dicc.get(p[1],False):
    if dicc.get(p[1]).get("tipo") != "LinkedList":
      errorSemantico = True
      res_sintactico.append( "ERROR SEMÁNTICO: TIPO DE VARIABLE NO ES LINKEDLIST")
  else:
    errorSemantico = True
    res_sintactico.append("ERROR SEMÁNTICO: ID NO DECLARADO")

def p_asignacion_const_i8(p):
  '''
  asignacion : CONST ID COLON INT8 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_i16(p):
  '''
  asignacion : CONST ID COLON INT16 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_i32(p):
  '''
  asignacion : CONST ID COLON INT32 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_i64(p):
  '''
  asignacion : CONST ID COLON INT64 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_i128(p):
  '''
  asignacion : CONST ID COLON INT128 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_ui8(p):
  '''
  asignacion : CONST ID COLON UINT8 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_ui16(p):
  '''
  asignacion : CONST ID COLON UINT16 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_ui32(p):
  '''
  asignacion : CONST ID COLON UINT32 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_ui64(p):
  '''
  asignacion : CONST ID COLON UINT64 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]
def p_asignacion_const_ui128(p):
  '''
  asignacion : CONST ID COLON UINT128 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_f32(p):
  '''
  asignacion : CONST ID COLON FLOAT32 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_asignacion_const_f64(p):
  '''
  asignacion : CONST ID COLON FLOAT64 IGUAL INTTYPE ENDCHAR
  '''
  global dicc
  dicc[p[2]] = p[4]

def p_sumaint(p):
  'sumaint : ID PLUS ID'
  global res_sintactico
  global dicc
  global errorSemantico
  if dicc.get(p[1])!=dicc.get(p[3]):
    errorSemantico = True
    res_sintactico.append( "ERROR SEMÁNTICO: NO SE PUEDE SUMAR ENTEROS DIFERENTES TAMAÑOS")



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
def validacion(f):
    global res_sintactico, errorSemantico
    entrada = input.get("1.0","end-1c")
    print(entrada)
    numeroLinea=1
    f.write(entrada + "\n") 

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
    now = datetime.now(timezone('EST')) 
    file = open('logfile.txt', 'a')
    file.write("\n-----Análisis Sintáctico/Semántico - Timestamp: " + str(now) +"\nEntrada: ")   
    validacion(file)
    resultado["text"] = "\n".join(res_sintactico)
    file.write("\n".join(res_sintactico))
    res_sintactico = []
    file.close()

def lex():
    now = datetime.now(timezone('EST')) 
    file = open('logfile.txt', 'a')
    file.write("\n----------Análisis Léxico - Timestamp: "+  str(now) + "\n Entrada: ")
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
  resultado["text"] = "Memoria limpiada"

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
resultado.pack(pady=20)


botonSemantic = tk.Button(second_frame, text = "Análisis semántico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSemantic.pack(pady=8)
botonSintac = tk.Button(second_frame, text = "Análisis sintáctico", padx=60,pady=10, command=sintactico, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonSintac.pack(pady=8)
botonLex = tk.Button(second_frame, text = "Análisis léxico", padx=60,pady=10, command=lex, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") #pasar funcion sin parentesis con command =
botonLex.pack(pady=8)
botonDicc = tk.Button(second_frame, text = "Limpiar Variables", padx=60,pady=10, command=limpiar, bg="#3b554f", fg="#d4eee8", font="Helvetica 12") 
botonDicc.pack()
root.title("bg attribute")
root['bg'] = '#f4fbf9'
root.mainloop()