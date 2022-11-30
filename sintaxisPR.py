#Analizador Sintactico: Pamela Rugel



#Conjunto de tipos de datos de asignacion
def p_valor(p):
  '''valor : valornumerico
  | TRUE
  | FALSE
  | ID
  | IDCHAR
  | IDSTRING
  | expresion
  | conectores
  | comparacion
  '''
  p[0] = p[1 ]

#Conjunto de estructuras de datos
def p_estructuras(p):
    '''
    estructuras : linkedlist
    | hashmap
    '''


# Estructura de control While
def p_while(p):
  'while : WHILE ifparams LLLAVE cuerpof RLLAVE'


#Estructura HASHMAP
def p_hashmap(p):
  'hashmap : HASHMAP DOSDOBLEPUNTOS NEW LPAREN RPAREN'

#Expresiones aritméticas
def p_expresion(p):
  'expresion :  valornumerico signo valornumerico'

#Valores para las expresiones aritméticas
def p_valornumerico(p):
  '''
  valornumerico : NINTTYPE
  | INTTYPE
  | FLOATTYPE
  | NFLOATTYPE
  '''
  p[0] = p[1]
  
def p_signo(p):
  '''
  signo : PLUS
  | TIMES
  | MINUS
  | PORCENTAJE
  | DIVIDE
  '''
  p[0] = p[1]

def p_entrada(p):
  '''
  entrada : IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN ENDCHAR
  | IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN POINT EXPECT LPAREN IDSTRING RPAREN ENDCHAR
  '''