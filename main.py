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
