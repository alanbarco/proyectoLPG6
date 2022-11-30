#Analizador Sintactico: José Jaramillo
#Asignacion   #const

def p_cuerpof(p):
  '''
  cuerpof : metodo
  | metodo cuerpof
  ''' 


def p_datatype(p):
  '''
  datatype : intsize
  | uintsize
  | floatsize
  | strsize
  | STRING
  | BOOL'''
  p[0] = p[1]

def p_intsize(p):
  '''
  intsize : INT8
  | INT16
  | INT32
  | INT64
  | INT128'''
  p[0] = p[1]

def p_floatsize(p):
  '''
  floatsize : FLOAT32
  | FLOAT64'''

  p[0] = p[1]

def p_uintsize(p):
  '''
  uintsize : UINT8
  | UINT16
  | UINT32
  | UINT64
  | UINT128'''
  p[0] = p[1]

def p_strsize(p):
  '''
  strsize : AMPERSAND COMILLA STATIC STR
  | AMPERSAND STR
  '''
def p_boolean(p):
  '''
  boolean : TRUE
  | FALSE
  '''
  p[0] = p[1]
#VEC

#CONDICION IF ELSE
def p_ifparams(p):
  '''
  ifparams : ifcondicion
  | boolean
  | ID
  ''' 

def p_elseblock(p):
  '''
  elseblock : ifblock ELSE LLLAVE cuerpof RLLAVE
  | elseifblock ELSE LLLAVE cuerpof RLLAVE
  '''

def p_elseifblock(p):
  '''
  elseifblock : ifblock ELSE IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE
  | ifblock ELSE IF ifparams LLLAVE cuerpof RLLAVE
  '''

def p_ifblock(p):
  '''
  ifblock : IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE
  | IF ifparams LLLAVE cuerpof RLLAVE
  ''' 

def p_ifcondicion(p):
  '''
  ifcondicion : comparacion
  | comparacion signoconect ifcondicion
  | LPAREN comparacion RPAREN
  | LPAREN comparacion RPAREN signoconect ifcondicion
  | LPAREN ifcondicion RPAREN
  '''

#TIPO DE FUNCION

#2. Definicion de funcion
  

def p_funcion_retorno(p):
  '''
  funcion : FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof RETURN ifparams ENDCHAR  RLLAVE
  '''

def p_funcion_returnimplicito(p):
  '''
  funcion : FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof ID RLLAVE
  '''

