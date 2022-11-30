
def p_cuerpo(p):
  '''cuerpo : metodo
  | funcion'''

def p_metodo(p):
  '''metodo : asignacion
  | impresion
  | loop
  | ifblock
  | elseifblock
  | elseblock
  | vectorpush
  | llpushfront
  | llpopback
  | sumaint
  | entrada
  | while
  '''

def p_comparacion_id(p):
  '''comparacion : ID signocompar ID
  | IDCHAR signocompar IDCHAR
  | IDSTRING signocompar IDSTRING'''

def p_comparacion_int(p):
  '''comparacion : INTTYPE signocompar INTTYPE
  | NINTTYPE signocompar NINTTYPE
  | FLOATTYPE signocompar FLOATTYPE
  '''
def p_comparacion_bool(p):
  'comparacion : boolean signocompar boolean'

def p_valor(p):
  '''valor : INTTYPE
  | FLOATTYPE
  | NINTTYPE
  | ID
  | TRUE
  | FALSE
  | IDCHAR
  | IDSTRING'''
  p[0] = p[1]

def p_signocompar(p):
  '''signocompar : MAYORQUE 
  | MENORQUE
  | DIFERENTE
  | IDENTICO
  '''
  
def p_linkedlist(p):
  'linkedlist : LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'

def p_conectores(p):
  '''conectores : boolean signoconect boolean 
  | EXCLAM boolean
  | ID signoconect ID'''

def p_signoconect(p):
  '''signoconect : DAMPERSAND
  | OR
  '''
def p_boolean(p):
  '''
  boolean : TRUE
  | FALSE
  '''
  p[0] =  p[1]
  
def p_loop(p):
  'loop : LOOP LLLAVE metodo RLLAVE'

def p_params(p):
  '''params : ID COLON datatype 
  | ID COLON datatype COMA params'''

def p_funcion_sinreturn(p):
  'funcion : FN ID LPAREN params RPAREN LLLAVE metodo RLLAVE'

def p_impresion(p):
  'impresion : PRINTLN LPAREN IDSTRING RPAREN ENDCHAR'
 

