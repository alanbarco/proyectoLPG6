import ply.lex as lex
'''
    RUST lexer
    Grupo 6
    Alan Barco
    José Javier Jaramillo Saltos
    Pamela Rugel

'''

#Agregue todas las palabras reservadas necesarias
# List of token names
reserved = {
  "async":'ASYNC',  "await":'AWAIT',        #Empieza Alan Barco
  "break": 'BREAK',
  "const": 'CONST',  "continue": 'CONTINUE',
  "dyn": 'DYN',
  "enum":'ENUM',    
  "fn": 'FN',    "final":'FINAL',    "for": "FOR",    "format": 'FORMAT',
  "in": 'IN',    "impl": 'IMPL',
  "loop": 'LOOP',
  "pub": 'PUB',  "priv":'PRIV',
  "ref": 'REF',  "return":'RETURN',
  "self": 'SELF',  "struct": 'STRUCT',  "sizeof":'SIZEOF',  "super":'SUPER',
  "type":'TYPE',  "typeof":'TYPEOF',
  "use": 'USE',  "unsafe":'UNSAFE',  
  "match":'MATCH',  "move":'MOVE',
  "where": 'WHERE',  
  "new" : "NEW",

  #Control statements
  "if": 'IF',
  "else": 'ELSE',

  #Data type and declarations
  "let": 'LET',
  "mut": 'MUT',
  "bool": 'BOOL',
  "f32": 'FLOAT32',
  "f64": 'FLOAT64',
  "i8": 'INT8',
  "i16": 'INT116',
  "i32": 'INT32',
  "i64": 'INT64',
  "i128": 'INT128',
  "str": 'STR',
  "char": 'CHAR',
  "String": 'STRING',
  "u8": 'UINT8',
  "u16": 'UINT16',
  "u32": 'UINT32',
  "u64": 'UINT64',
  "u128": 'UINT128',
  "usize": 'POINTERSIZE',

  #Some reserved functions
  "Err": 'ERR',
  "println\!": 'PRINTLN',
  "input": 'INPUT',
  "excpect": 'EXPECT',
  "parse": 'PARSE',
  "unwrap_or": "UNWRAPOR",
  "Ok": 'OK',
  "main": 'MAINFN',

  #Data structures
  "Vec" : 'VEC',
  "HashMap" : 'HASHMAP',
  "LinkedList" : 'LINKEDLIST'           #Termina Alan Barco
}

tokens = [                          #Empieza Pamela Rugel
  'AMPERSAND',
  'COMILLA',
  'PLUS',
  'MINUS',
  'TIMES',
  'DAMPERSAND',
  'DIVIDE',
  'IGUAL',
  'ARROWOPT',
  'MAYORQUE',
  'MENORQUE',
  'LCOR',
  'RCOR',
  'LPAREN',
  'RPAREN',
  'LLLAVE',
  'RLLAVE',
  'COLON',
  'ENDCHAR',
  'COMA',
  'INTERRO',
  'EXCLAM',
  'POINT',
  'TRUE',
  'FALSE',
  'IDCHAR',
  'NINTTYPE',
  'INTTYPE',
  'FLOATTYPE',
  'IDSTRING',
  'ID',
  'DIFERENTE',
  'SUMAASIGN',
  'RESTAASIGN',
  'DIVASIGN',
  'MULTIASIGN',
  'DOLAR',
  'DOSDOBLEPUNTOS',
  'PORCENTAJE'
  
  
  
] + list(reserved.values())          #Termina Pamela Rugel

                                  #Empieza José Jaramillo

#Agregue sus Expresiones Regulares y o Funciones
t_DAMPERSAND= r'&&'
t_AMPERSAND = r'&'
t_COMILLA = r"'"
t_ARROWOPT = r'->'
t_COLON = r':'
t_COMA = r','
t_DIVIDE = r'/'
t_ENDCHAR = r';'
t_EXCLAM = r'!'
t_IDCHAR = r"('[^']?'|'\\'')"
t_IDSTRING = r'"([^"]|\\")*"'
t_IGUAL = r'='
t_INTERRO = r'\?'
t_LCOR = r'\['
t_LLLAVE = r'\{'
t_LPAREN = r'\('
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MINUS = r'-'
t_PLUS = r'\+'
t_POINT = r'\.'
t_RCOR = r'\]'
t_RLLAVE = r'\}'
t_RPAREN = r'\)'
t_TIMES = r'\*'
t_DIFERENTE = r'!='
t_SUMAASIGN = r'\+='
t_RESTAASIGN = r'-='
t_DIVASIGN = r'/='
t_MULTIASIGN = r'\*='
t_DOLAR = r'\$'
t_DOSDOBLEPUNTOS = r'\::'
t_PORCENTAJE = r'%'                         



def t_FLOATTYPE(t):                         
  r"\d+\.\d*"
  t.value = float(t.value)
  return t


def t_INTTYPE(t):
  r'-\d+'
  t.value = int(t.value)
  return t


def t_NINTTYPE(t):
  r'\d+'
  t.value = int(t.value)
  return t


def t_TRUE(t):
  r"true"
  t.value = True
  return t


def t_FALSE(t):
  r"false"
  t.value = False
  return t


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t

 #HASTA AQUI BORRE

  
# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


def t_COMMENT(t):
  r'(//.*|/\*(.*|\n*)*\*/)'
  pass                             #Termina José Jaramillo

# Build the lexer
lexer = lex.lex()

# Tokenize
file = open("source.txt")
cadena = file.read()
file.close()
lexer.input(cadena)

output_file = open('result.txt', 'w') 
line_number = 1

while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok)
  if line_number != tok.lineno:
    output_file.write("\n")
    line_number = tok.lineno
  output_file.write(tok.type)
  output_file.write("  ")

output_file.close()

print("Ingreso de Tokens por consola")
linea = " "
while linea != "":
  linea = input(">>")
  lexer.input(linea)
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok)
# Tokenize
print("Succesfull")