
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
  | entrada
  | while
  '''

def p_comparacion(p):
  'comparacion : valorescomp signocompar valorescomp'

def p_signocompar(p):
  '''signocompar : MAYORQUE 
  | MENORQUE
  | DIFERENTE
  | IDENTICO
  '''

def p_valorecomp(p):
  '''valorescomp : ID
  | IDCHAR
  | IDSTRING
  | INTTYPE
  | NINTTYPE
  | FLOATTYPE
  | NFLOATTYPE
  | boolean
  '''
  
def p_linkedlist(p):
  'linkedlist : LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN'

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
def p_loop(p):
  'loop : LOOP LLLAVE metodo RLLAVE'

def p_params(p):
  '''params : ID COLON datatype 
  | ID COLON datatype COMA params'''

def p_funcion_sinreturn(p):
  'funcion : FN ID LPAREN params RPAREN LLLAVE metodo RLLAVE'

def p_impresion(p):
  'impresion : PRINTLN LPAREN IDSTRING RPAREN ENDCHAR'
 
 # Build the parser
