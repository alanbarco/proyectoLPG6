import ply.lex as lex
import ply.yacc as yacc
from lexico import tokens
from sintaxis import *
from datetime import datetime
from pytz import timezone


def p_error(p):
  cadena = " "
  if p:
    cadena =  f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    print(cadena)
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
  with open('logfile.txt', 'a') as file:
      file.write(cadena + "\n")  


now = datetime.now(timezone('EST')) 

parser = yacc.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)
  return result

'''while True:
  try:
    s = input('calc > ')
    with open('logfile.txt', 'a') as file:
      file.write("-------------------------\n")
      file.write("Entrada: " + "'"+s +"'" +" " + "Timestamp: " + str(now) +"\n")
    
  except EOFError:
    break
  if not s: continue
  validaRegla(s)
  with open('logfile.txt', 'a') as file:
      file.write("Resultado: "+ str(validaRegla(s)) + "\n")
      file.write("-------------------------\n")'''

