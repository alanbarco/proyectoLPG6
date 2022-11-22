import ply.yacc as yacc


def p_cuerpo(p):
  '''cuerpo : metodo
  | funcion'''

def p_metodo(p):
  '''metodo : asignacion
  | impresion
  | comparacion
  | linkedlist
  | loop
  | conectores
  '''

def p_asignacion(p):
  '''asignacion : LET MUT ID IGUAL valor ENDCHAR
  | LET ID IGUAL valor ENDCHAR
  | CONST ID IGUAL valor ENDCHAR'''


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

def p_signocompar(p):
  '''signocompar : MAYORQUE 
  | MENORQUE
  | DIFERENTE
  | IDENTICO
  '''
  
def p_linkedlist(p):
  'linkedlist : LET MUT ID IGUAL LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR'

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
  '''params : ID COLON INT16 
  | ID COLON INT16 COMA params'''

def p_funcion(p):
  'funcion : FN ID LPAREN params RPAREN LLLAVE metodo RLLAVE'

def p_impresion(p):
  'impresion : PRINTLN LPAREN valor RPAREN ENDCHAR'
 
 # Build the parser
