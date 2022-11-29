
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND ARROWOPT ASYNC AWAIT BOOL BREAK CHAR COLON COMA COMILLA CONST CONTINUE DAMPERSAND DIFERENTE DIVASIGN DIVIDE DOLAR DOSDOBLEPUNTOS DYN ELSE ENDCHAR ENUM ERR EXCLAM EXPECT FALSE FINAL FLOAT32 FLOAT64 FLOATTYPE FN FOR FORMAT FROM HASHMAP ID IDCHAR IDENTICO IDSTRING IF IGUAL IMPL IN INPUT INT128 INT16 INT32 INT64 INT8 INTERRO INTTYPE IO LCOR LET LINKEDLIST LLLAVE LOOP LPAREN MAINFN MATCH MAYORQUE MENORQUE MINUS MOVE MULTIASIGN MUT NEW NFLOATTYPE NINTTYPE OK OR PARSE PLUS POINT POINTERSIZE PORCENTAJE PRINTLN PRIV PUB RCOR READLINE REF RESTAASIGN RETURN RLLAVE RPAREN SELF SIZEOF STATIC STDIN STR STRING STRUCT SUMAASIGN SUPER TIMES TRUE TYPE TYPEOF UINT128 UINT16 UINT32 UINT64 UINT8 UNSAFE UNWRAPOR USE VEC WHERE WHILEcuerpo : metodo\n  | funcion\n  cuerpof : metodo\n  | metodo cuerpof\n  asignacion : LET MUT ID IGUAL valor ENDCHAR\n  | LET MUT ID IGUAL estructuras ENDCHARmetodo : asignacion\n  | impresion\n  | loop\n  | ifblock\n  | elseifblock\n  | elseblock\n  | entrada\n  | while\n  asignacion : LET ID IGUAL valor ENDCHAR\n  asignacion : CONST ID COLON intsize IGUAL INTTYPE ENDCHAR\n  | CONST ID COLON intsize IGUAL NINTTYPE ENDCHAR\n  valor : valornumerico\n  | TRUE\n  | FALSE\n  | ID\n  | IDCHAR\n  | IDSTRING\n  | expresion\n  | conectores\n  | comparacion\n  asignacion : CONST ID COLON uintsize IGUAL INTTYPE ENDCHARcomparacion : valorescomp signocompar valorescompasignacion : CONST ID COLON floatsize IGUAL FLOATTYPE ENDCHARsignocompar : MAYORQUE \n  | MENORQUE\n  | DIFERENTE\n  | IDENTICO\n  asignacion : CONST ID COLON strsize IGUAL IDSTRING ENDCHARasignacion : CONST ID COLON STRING IGUAL STRING DOSDOBLEPUNTOS FROM LPAREN IDSTRING RPAREN ENDCHAR\n    estructuras : linkedlist\n    | hashmap\n    | vec\n    asignacion : CONST ID COLON STRING IGUAL IDSTRING ENDCHARvalorescomp : ID\n  | IDCHAR\n  | IDSTRING\n  | INTTYPE\n  | NINTTYPE\n  | FLOATTYPE\n  | NFLOATTYPE\n  | boolean\n  asignacion : CONST ID COLON BOOL IGUAL boolean ENDCHARwhile : WHILE ifparams LLLAVE cuerpof RLLAVEasignacion : CONST ID COLON CHAR IGUAL IDCHAR ENDCHAR\n  datatype : intsize\n  | uintsize\n  | floatsize\n  | strsize\n  | STRINGhashmap : HASHMAP DOSDOBLEPUNTOS NEW LPAREN RPARENlinkedlist : LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHARconectores : boolean signoconect boolean \n  | EXCLAM boolean\n  | ID signoconect IDvec : VEC DOSDOBLEPUNTOS NEW LPAREN RPAREN\n  intsize : INT8\n  | INT16\n  | INT32\n  | INT64\n  | INT128expresion :  valornumerico signo valornumericosignoconect : DAMPERSAND\n  | OR\n  \n  valornumerico : NINTTYPE\n  | INTTYPE\n  | FLOATTYPE\n  | NFLOATTYPE\n  \n  floatsize : FLOAT32\n  | FLOAT64loop : LOOP LLLAVE metodo RLLAVE\n  signo : PLUS\n  | TIMES\n  | MINUS\n  | PORCENTAJE\n  | DIVIDE\n  params : ID COLON datatype \n  | ID COLON datatype COMA params\n  uintsize : UINT8\n  | UINT16\n  | UINT32\n  | UINT64\n  | UINT128funcion : FN ID LPAREN params RPAREN LLLAVE metodo RLLAVEimpresion : PRINTLN LPAREN IDSTRING RPAREN ENDCHAR\n  strsize : AMPERSAND COMILLA STATIC STR\n  | AMPERSAND STR\n  \n  entrada : IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN ENDCHAR\n  | IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN POINT EXPECT LPAREN IDSTRING RPAREN ENDCHAR\n  \n  boolean : TRUE\n  | FALSE\n  \n  ifparams : ifcondicion\n  | boolean\n  | ID\n  \n  elseblock : ifblock ELSE LLLAVE cuerpof RLLAVE\n  | elseifblock ELSE LLLAVE cuerpof RLLAVE\n  \n  elseifblock : ifblock ELSE IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE\n  | ifblock ELSE IF ifparams LLLAVE cuerpof RLLAVE\n  \n  ifblock : IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE\n  | IF ifparams LLLAVE cuerpof RLLAVE\n  \n  ifcondicion : comparacion\n  | comparacion signoconect ifcondicion\n  | LPAREN comparacion RPAREN\n  | LPAREN comparacion RPAREN signoconect ifcondicion\n  | LPAREN ifcondicion RPAREN\n  \n  funcion : FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof RETURN ifparams ENDCHAR  RLLAVE\n  \n  funcion : FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof ID RLLAVE\n  '
    
_lr_action_items = {'FN':([0,],[12,]),'LET':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[13,-7,-8,-9,-10,-11,-12,-13,-14,13,13,13,13,13,13,-76,13,-100,-101,-15,-90,13,-105,-49,13,-5,-6,13,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,13,-102,-35,-93,-94,]),'CONST':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[14,-7,-8,-9,-10,-11,-12,-13,-14,14,14,14,14,14,14,-76,14,-100,-101,-15,-90,14,-105,-49,14,-5,-6,14,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,14,-102,-35,-93,-94,]),'PRINTLN':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[15,-7,-8,-9,-10,-11,-12,-13,-14,15,15,15,15,15,15,-76,15,-100,-101,-15,-90,15,-105,-49,15,-5,-6,15,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,15,-102,-35,-93,-94,]),'LOOP':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[16,-7,-8,-9,-10,-11,-12,-13,-14,16,16,16,16,16,16,-76,16,-100,-101,-15,-90,16,-105,-49,16,-5,-6,16,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,16,-102,-35,-93,-94,]),'IF':([0,4,5,6,7,8,9,10,11,20,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[17,-7,-8,-9,-10,-11,-12,-13,-14,46,17,17,17,17,17,17,-76,17,-100,-101,-15,-90,17,-105,-49,17,-5,-6,17,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,17,-102,-35,-93,-94,]),'IO':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[18,-7,-8,-9,-10,-11,-12,-13,-14,18,18,18,18,18,18,-76,18,-100,-101,-15,-90,18,-105,-49,18,-5,-6,18,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,18,-102,-35,-93,-94,]),'WHILE':([0,4,5,6,7,8,9,10,11,27,47,48,58,68,75,117,127,128,130,142,160,161,163,165,174,176,177,201,202,209,210,211,212,213,215,216,217,219,224,230,247,251,256,],[19,-7,-8,-9,-10,-11,-12,-13,-14,19,19,19,19,19,19,-76,19,-100,-101,-15,-90,19,-105,-49,19,-5,-6,19,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,19,-102,-35,-93,-94,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,117,128,130,142,160,163,165,176,177,202,209,210,211,212,213,215,216,217,219,223,230,242,247,249,251,256,],[0,-1,-2,-7,-8,-9,-10,-11,-12,-13,-14,-76,-100,-101,-15,-90,-105,-49,-5,-6,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,-89,-102,-112,-35,-111,-93,-94,]),'RLLAVE':([4,5,6,7,8,9,10,11,54,74,75,76,117,121,125,128,129,130,142,160,163,165,167,176,177,198,202,204,209,210,211,212,213,215,216,217,219,221,230,237,246,247,251,256,],[-7,-8,-9,-10,-11,-12,-13,-14,117,128,-3,130,-76,163,165,-100,-4,-101,-15,-90,-105,-49,202,-5,-6,219,-103,223,-16,-17,-27,-29,-34,-39,-48,-50,-104,230,-102,242,249,-35,-93,-94,]),'RETURN':([4,5,6,7,8,9,10,11,75,117,128,129,130,142,160,163,165,176,177,202,209,210,211,212,213,215,216,217,219,230,231,247,251,256,],[-7,-8,-9,-10,-11,-12,-13,-14,-3,-76,-100,-4,-101,-15,-90,-105,-49,-5,-6,-103,-16,-17,-27,-29,-34,-39,-48,-50,-104,-102,238,-35,-93,-94,]),'ID':([4,5,6,7,8,9,10,11,12,13,14,17,19,23,28,45,46,49,51,59,60,61,62,63,64,65,66,72,75,79,117,128,129,130,141,142,160,162,163,165,176,177,202,203,209,210,211,212,213,215,216,217,219,230,231,238,241,247,251,256,],[-7,-8,-9,-10,-11,-12,-13,-14,22,24,25,32,32,50,32,70,32,77,80,70,-68,-69,70,-30,-31,-32,-33,32,-3,80,-76,-100,-4,-101,181,-15,-90,70,-105,-49,-5,-6,-103,77,-16,-17,-27,-29,-34,-39,-48,-50,-104,-102,237,32,245,-35,-93,-94,]),'ELSE':([7,8,163,202,219,230,],[20,21,-105,-103,-104,-102,]),'MUT':([13,236,],[23,241,]),'LPAREN':([15,17,19,22,28,45,46,59,60,61,67,72,162,206,207,208,220,228,238,252,],[26,28,45,49,45,45,72,45,-68,-69,124,45,45,225,226,227,229,235,45,253,]),'LLLAVE':([16,20,21,29,30,31,32,33,34,35,37,38,39,40,41,42,44,70,71,73,103,104,105,106,107,108,109,110,111,112,113,114,118,119,120,122,123,132,159,166,169,170,171,172,173,199,205,218,],[27,47,48,58,-97,-98,-99,-106,-95,-96,-41,-42,-43,-44,-45,-46,68,-40,-47,127,-62,-63,-64,-65,-66,-84,-85,-86,-87,-88,-74,-75,161,-108,-110,-107,-28,174,-92,201,-51,-52,-53,-54,-55,-109,224,-91,]),'TRUE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,95,149,156,162,238,],[34,34,34,34,34,83,34,-68,-69,34,-30,-31,-32,-33,34,83,34,34,34,34,34,]),'FALSE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,95,149,156,162,238,],[35,35,35,35,35,84,35,-68,-69,35,-30,-31,-32,-33,35,84,35,35,35,35,35,]),'IDCHAR':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,157,162,238,],[37,37,37,37,37,85,37,-68,-69,37,-30,-31,-32,-33,37,85,196,37,37,]),'IDSTRING':([17,19,26,28,45,46,51,59,60,61,62,63,64,65,66,72,79,154,155,162,235,238,253,],[38,38,53,38,38,38,86,38,-68,-69,38,-30,-31,-32,-33,38,86,192,194,38,240,38,254,]),'INTTYPE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,143,144,145,146,147,148,151,152,162,238,],[39,39,39,39,39,91,39,-68,-69,39,-30,-31,-32,-33,39,91,184,-77,-78,-79,-80,-81,188,190,39,39,]),'NINTTYPE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,143,144,145,146,147,148,151,162,238,],[40,40,40,40,40,90,40,-68,-69,40,-30,-31,-32,-33,40,90,183,-77,-78,-79,-80,-81,189,40,40,]),'FLOATTYPE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,143,144,145,146,147,148,153,162,238,],[41,41,41,41,41,92,41,-68,-69,41,-30,-31,-32,-33,41,92,185,-77,-78,-79,-80,-81,191,41,41,]),'NFLOATTYPE':([17,19,28,45,46,51,59,60,61,62,63,64,65,66,72,79,143,144,145,146,147,148,162,238,],[42,42,42,42,42,93,42,-68,-69,42,-30,-31,-32,-33,42,93,186,-77,-78,-79,-80,-81,42,42,]),'DOSDOBLEPUNTOS':([18,138,139,140,193,],[43,178,179,180,214,]),'IGUAL':([24,50,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,159,218,],[51,79,151,152,153,154,155,156,157,-62,-63,-64,-65,-66,-84,-85,-86,-87,-88,-74,-75,-92,-91,]),'COLON':([25,77,],[52,131,]),'ENDCHAR':([30,31,32,33,34,35,37,38,39,40,41,42,70,71,80,81,82,83,84,85,86,87,88,89,90,91,92,93,116,119,120,122,123,133,134,135,136,137,150,181,182,183,184,185,186,187,188,189,190,191,192,194,195,196,199,232,233,234,239,243,244,248,255,],[-97,-98,-99,-106,-95,-96,-41,-42,-43,-44,-45,-46,-40,-47,-21,142,-18,-19,-20,-22,-23,-24,-25,-26,-70,-71,-72,-73,160,-108,-110,-107,-28,176,177,-36,-37,-38,-59,-60,-67,-70,-71,-72,-73,-58,209,210,211,212,213,215,216,217,-109,239,-56,-61,-57,246,247,251,256,]),'RPAREN':([31,32,33,34,35,37,38,39,40,41,42,53,55,56,57,69,70,71,78,103,104,105,106,107,108,109,110,111,112,113,114,119,120,122,123,124,126,159,168,169,170,171,172,173,199,218,222,225,226,227,240,245,254,],[-98,-99,-106,-95,-96,-41,-42,-43,-44,-45,-46,116,118,119,120,120,-40,-47,132,-62,-63,-64,-65,-66,-84,-85,-86,-87,-88,-74,-75,-108,-110,-107,-28,164,166,-92,-82,-51,-52,-53,-54,-55,-109,-91,-83,232,233,234,244,248,255,]),'MAYORQUE':([31,32,34,35,36,37,38,39,40,41,42,70,71,80,83,84,85,86,90,91,92,93,94,],[-47,-40,-95,-96,63,-41,-42,-43,-44,-45,-46,-40,-47,-40,-95,-96,-41,-42,-44,-43,-45,-46,-47,]),'MENORQUE':([31,32,34,35,36,37,38,39,40,41,42,70,71,80,83,84,85,86,90,91,92,93,94,],[-47,-40,-95,-96,64,-41,-42,-43,-44,-45,-46,-40,-47,-40,-95,-96,-41,-42,-44,-43,-45,-46,-47,]),'DIFERENTE':([31,32,34,35,36,37,38,39,40,41,42,70,71,80,83,84,85,86,90,91,92,93,94,],[-47,-40,-95,-96,65,-41,-42,-43,-44,-45,-46,-40,-47,-40,-95,-96,-41,-42,-44,-43,-45,-46,-47,]),'IDENTICO':([31,32,34,35,36,37,38,39,40,41,42,70,71,80,83,84,85,86,90,91,92,93,94,],[-47,-40,-95,-96,66,-41,-42,-43,-44,-45,-46,-40,-47,-40,-95,-96,-41,-42,-44,-43,-45,-46,-47,]),'DAMPERSAND':([33,34,35,37,38,39,40,41,42,56,70,71,80,83,84,94,119,123,],[60,-95,-96,-41,-42,-43,-44,-45,-46,60,-40,-47,60,-95,-96,60,60,-28,]),'OR':([33,34,35,37,38,39,40,41,42,56,70,71,80,83,84,94,119,123,],[61,-95,-96,-41,-42,-43,-44,-45,-46,61,-40,-47,61,-95,-96,61,61,-28,]),'STDIN':([43,],[67,]),'EXCLAM':([51,79,],[95,95,]),'STRING':([52,131,155,175,],[100,173,193,173,]),'BOOL':([52,],[101,]),'CHAR':([52,],[102,]),'INT8':([52,131,175,],[103,103,103,]),'INT16':([52,131,175,],[104,104,104,]),'INT32':([52,131,175,],[105,105,105,]),'INT64':([52,131,175,],[106,106,106,]),'INT128':([52,131,175,],[107,107,107,]),'UINT8':([52,131,175,],[108,108,108,]),'UINT16':([52,131,175,],[109,109,109,]),'UINT32':([52,131,175,],[110,110,110,]),'UINT64':([52,131,175,],[111,111,111,]),'UINT128':([52,131,175,],[112,112,112,]),'FLOAT32':([52,131,175,],[113,113,113,]),'FLOAT64':([52,131,175,],[114,114,114,]),'AMPERSAND':([52,131,175,229,],[115,115,115,236,]),'LINKEDLIST':([79,],[138,]),'HASHMAP':([79,],[139,]),'VEC':([79,],[140,]),'PLUS':([82,90,91,92,93,],[144,-70,-71,-72,-73,]),'TIMES':([82,90,91,92,93,],[145,-70,-71,-72,-73,]),'MINUS':([82,90,91,92,93,],[146,-70,-71,-72,-73,]),'PORCENTAJE':([82,90,91,92,93,],[147,-70,-71,-72,-73,]),'DIVIDE':([82,90,91,92,93,],[148,-70,-71,-72,-73,]),'COMA':([103,104,105,106,107,108,109,110,111,112,113,114,159,168,169,170,171,172,173,218,],[-62,-63,-64,-65,-66,-84,-85,-86,-87,-88,-74,-75,-92,203,-51,-52,-53,-54,-55,-91,]),'COMILLA':([115,],[158,]),'STR':([115,197,],[159,218,]),'ARROWOPT':([132,],[175,]),'STATIC':([158,],[197,]),'POINT':([164,248,],[200,250,]),'NEW':([178,179,180,],[206,207,208,]),'READLINE':([200,],[220,]),'FROM':([214,],[228,]),'EXPECT':([250,],[252,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'metodo':([0,27,47,48,58,68,75,127,161,174,201,224,],[2,54,75,75,75,75,75,75,75,204,75,75,]),'funcion':([0,],[3,]),'asignacion':([0,27,47,48,58,68,75,127,161,174,201,224,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'impresion':([0,27,47,48,58,68,75,127,161,174,201,224,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'loop':([0,27,47,48,58,68,75,127,161,174,201,224,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'ifblock':([0,27,47,48,58,68,75,127,161,174,201,224,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'elseifblock':([0,27,47,48,58,68,75,127,161,174,201,224,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'elseblock':([0,27,47,48,58,68,75,127,161,174,201,224,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'entrada':([0,27,47,48,58,68,75,127,161,174,201,224,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'while':([0,27,47,48,58,68,75,127,161,174,201,224,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'ifparams':([17,19,28,46,72,238,],[29,44,55,73,126,243,]),'ifcondicion':([17,19,28,45,46,59,72,162,238,],[30,30,57,69,30,122,57,199,30,]),'boolean':([17,19,28,45,46,51,59,62,72,79,95,149,156,162,238,],[31,31,31,71,31,94,71,71,31,94,150,187,195,71,31,]),'comparacion':([17,19,28,45,46,51,59,72,79,162,238,],[33,33,56,56,33,89,33,56,89,33,33,]),'valorescomp':([17,19,28,45,46,51,59,62,72,79,162,238,],[36,36,36,36,36,36,36,123,36,36,36,36,]),'signoconect':([33,56,80,94,119,],[59,59,141,149,162,]),'signocompar':([36,],[62,]),'cuerpof':([47,48,58,68,75,127,161,201,224,],[74,76,121,125,129,167,198,221,231,]),'params':([49,203,],[78,222,]),'valor':([51,79,],[81,133,]),'valornumerico':([51,79,143,],[82,82,182,]),'expresion':([51,79,],[87,87,]),'conectores':([51,79,],[88,88,]),'intsize':([52,131,175,],[96,169,169,]),'uintsize':([52,131,175,],[97,170,170,]),'floatsize':([52,131,175,],[98,171,171,]),'strsize':([52,131,175,],[99,172,172,]),'estructuras':([79,],[134,]),'linkedlist':([79,],[135,]),'hashmap':([79,],[136,]),'vec':([79,],[137,]),'signo':([82,],[143,]),'datatype':([131,175,],[168,205,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> metodo','cuerpo',1,'p_cuerpo','sintaxisAB.py',3),
  ('cuerpo -> funcion','cuerpo',1,'p_cuerpo','sintaxisAB.py',4),
  ('cuerpof -> metodo','cuerpof',1,'p_cuerpof','sintaxisJJ.py',6),
  ('cuerpof -> metodo cuerpof','cuerpof',2,'p_cuerpof','sintaxisJJ.py',7),
  ('asignacion -> LET MUT ID IGUAL valor ENDCHAR','asignacion',6,'p_asignacion_let_mut','sintaxisPR.py',5),
  ('asignacion -> LET MUT ID IGUAL estructuras ENDCHAR','asignacion',6,'p_asignacion_let_mut','sintaxisPR.py',6),
  ('metodo -> asignacion','metodo',1,'p_metodo','sintaxisAB.py',7),
  ('metodo -> impresion','metodo',1,'p_metodo','sintaxisAB.py',8),
  ('metodo -> loop','metodo',1,'p_metodo','sintaxisAB.py',9),
  ('metodo -> ifblock','metodo',1,'p_metodo','sintaxisAB.py',10),
  ('metodo -> elseifblock','metodo',1,'p_metodo','sintaxisAB.py',11),
  ('metodo -> elseblock','metodo',1,'p_metodo','sintaxisAB.py',12),
  ('metodo -> entrada','metodo',1,'p_metodo','sintaxisAB.py',13),
  ('metodo -> while','metodo',1,'p_metodo','sintaxisAB.py',14),
  ('asignacion -> LET ID IGUAL valor ENDCHAR','asignacion',5,'p_asignacion_let','sintaxisPR.py',10),
  ('asignacion -> CONST ID COLON intsize IGUAL INTTYPE ENDCHAR','asignacion',7,'p_asignacion_const_int','sintaxisJJ.py',12),
  ('asignacion -> CONST ID COLON intsize IGUAL NINTTYPE ENDCHAR','asignacion',7,'p_asignacion_const_int','sintaxisJJ.py',13),
  ('valor -> valornumerico','valor',1,'p_valor','sintaxisPR.py',14),
  ('valor -> TRUE','valor',1,'p_valor','sintaxisPR.py',15),
  ('valor -> FALSE','valor',1,'p_valor','sintaxisPR.py',16),
  ('valor -> ID','valor',1,'p_valor','sintaxisPR.py',17),
  ('valor -> IDCHAR','valor',1,'p_valor','sintaxisPR.py',18),
  ('valor -> IDSTRING','valor',1,'p_valor','sintaxisPR.py',19),
  ('valor -> expresion','valor',1,'p_valor','sintaxisPR.py',20),
  ('valor -> conectores','valor',1,'p_valor','sintaxisPR.py',21),
  ('valor -> comparacion','valor',1,'p_valor','sintaxisPR.py',22),
  ('asignacion -> CONST ID COLON uintsize IGUAL INTTYPE ENDCHAR','asignacion',7,'p_asignacion_const_uint','sintaxisJJ.py',17),
  ('comparacion -> valorescomp signocompar valorescomp','comparacion',3,'p_comparacion','sintaxisAB.py',18),
  ('asignacion -> CONST ID COLON floatsize IGUAL FLOATTYPE ENDCHAR','asignacion',7,'p_asignacion_const_float','sintaxisJJ.py',20),
  ('signocompar -> MAYORQUE','signocompar',1,'p_signocompar','sintaxisAB.py',23),
  ('signocompar -> MENORQUE','signocompar',1,'p_signocompar','sintaxisAB.py',24),
  ('signocompar -> DIFERENTE','signocompar',1,'p_signocompar','sintaxisAB.py',25),
  ('signocompar -> IDENTICO','signocompar',1,'p_signocompar','sintaxisAB.py',26),
  ('asignacion -> CONST ID COLON strsize IGUAL IDSTRING ENDCHAR','asignacion',7,'p_asignacion_const_str','sintaxisJJ.py',23),
  ('asignacion -> CONST ID COLON STRING IGUAL STRING DOSDOBLEPUNTOS FROM LPAREN IDSTRING RPAREN ENDCHAR','asignacion',12,'p_asignacion_const_string','sintaxisJJ.py',26),
  ('estructuras -> linkedlist','estructuras',1,'p_estructuras','sintaxisPR.py',28),
  ('estructuras -> hashmap','estructuras',1,'p_estructuras','sintaxisPR.py',29),
  ('estructuras -> vec','estructuras',1,'p_estructuras','sintaxisPR.py',30),
  ('asignacion -> CONST ID COLON STRING IGUAL IDSTRING ENDCHAR','asignacion',7,'p_asignacion_const_string2','sintaxisJJ.py',29),
  ('valorescomp -> ID','valorescomp',1,'p_valorescomp','sintaxisAB.py',30),
  ('valorescomp -> IDCHAR','valorescomp',1,'p_valorescomp','sintaxisAB.py',31),
  ('valorescomp -> IDSTRING','valorescomp',1,'p_valorescomp','sintaxisAB.py',32),
  ('valorescomp -> INTTYPE','valorescomp',1,'p_valorescomp','sintaxisAB.py',33),
  ('valorescomp -> NINTTYPE','valorescomp',1,'p_valorescomp','sintaxisAB.py',34),
  ('valorescomp -> FLOATTYPE','valorescomp',1,'p_valorescomp','sintaxisAB.py',35),
  ('valorescomp -> NFLOATTYPE','valorescomp',1,'p_valorescomp','sintaxisAB.py',36),
  ('valorescomp -> boolean','valorescomp',1,'p_valorescomp','sintaxisAB.py',37),
  ('asignacion -> CONST ID COLON BOOL IGUAL boolean ENDCHAR','asignacion',7,'p_asignacion_const_bool','sintaxisJJ.py',34),
  ('while -> WHILE ifparams LLLAVE cuerpof RLLAVE','while',5,'p_while','sintaxisPR.py',35),
  ('asignacion -> CONST ID COLON CHAR IGUAL IDCHAR ENDCHAR','asignacion',7,'p_asignacion_const_char','sintaxisJJ.py',37),
  ('datatype -> intsize','datatype',1,'p_datatype','sintaxisJJ.py',41),
  ('datatype -> uintsize','datatype',1,'p_datatype','sintaxisJJ.py',42),
  ('datatype -> floatsize','datatype',1,'p_datatype','sintaxisJJ.py',43),
  ('datatype -> strsize','datatype',1,'p_datatype','sintaxisJJ.py',44),
  ('datatype -> STRING','datatype',1,'p_datatype','sintaxisJJ.py',45),
  ('hashmap -> HASHMAP DOSDOBLEPUNTOS NEW LPAREN RPAREN','hashmap',5,'p_hashmap','sintaxisPR.py',40),
  ('linkedlist -> LINKEDLIST DOSDOBLEPUNTOS NEW LPAREN RPAREN ENDCHAR','linkedlist',6,'p_linkedlist','sintaxisAB.py',41),
  ('conectores -> boolean signoconect boolean','conectores',3,'p_conectores','sintaxisAB.py',44),
  ('conectores -> EXCLAM boolean','conectores',2,'p_conectores','sintaxisAB.py',45),
  ('conectores -> ID signoconect ID','conectores',3,'p_conectores','sintaxisAB.py',46),
  ('vec -> VEC DOSDOBLEPUNTOS NEW LPAREN RPAREN','vec',5,'p_vec','sintaxisPR.py',44),
  ('intsize -> INT8','intsize',1,'p_intsize','sintaxisJJ.py',49),
  ('intsize -> INT16','intsize',1,'p_intsize','sintaxisJJ.py',50),
  ('intsize -> INT32','intsize',1,'p_intsize','sintaxisJJ.py',51),
  ('intsize -> INT64','intsize',1,'p_intsize','sintaxisJJ.py',52),
  ('intsize -> INT128','intsize',1,'p_intsize','sintaxisJJ.py',53),
  ('expresion -> valornumerico signo valornumerico','expresion',3,'p_expresion','sintaxisPR.py',48),
  ('signoconect -> DAMPERSAND','signoconect',1,'p_signoconect','sintaxisAB.py',49),
  ('signoconect -> OR','signoconect',1,'p_signoconect','sintaxisAB.py',50),
  ('valornumerico -> NINTTYPE','valornumerico',1,'p_valornumerico','sintaxisPR.py',53),
  ('valornumerico -> INTTYPE','valornumerico',1,'p_valornumerico','sintaxisPR.py',54),
  ('valornumerico -> FLOATTYPE','valornumerico',1,'p_valornumerico','sintaxisPR.py',55),
  ('valornumerico -> NFLOATTYPE','valornumerico',1,'p_valornumerico','sintaxisPR.py',56),
  ('floatsize -> FLOAT32','floatsize',1,'p_floatsize','sintaxisJJ.py',57),
  ('floatsize -> FLOAT64','floatsize',1,'p_floatsize','sintaxisJJ.py',58),
  ('loop -> LOOP LLLAVE metodo RLLAVE','loop',4,'p_loop','sintaxisAB.py',58),
  ('signo -> PLUS','signo',1,'p_signo','sintaxisPR.py',61),
  ('signo -> TIMES','signo',1,'p_signo','sintaxisPR.py',62),
  ('signo -> MINUS','signo',1,'p_signo','sintaxisPR.py',63),
  ('signo -> PORCENTAJE','signo',1,'p_signo','sintaxisPR.py',64),
  ('signo -> DIVIDE','signo',1,'p_signo','sintaxisPR.py',65),
  ('params -> ID COLON datatype','params',3,'p_params','sintaxisAB.py',61),
  ('params -> ID COLON datatype COMA params','params',5,'p_params','sintaxisAB.py',62),
  ('uintsize -> UINT8','uintsize',1,'p_uintsize','sintaxisJJ.py',62),
  ('uintsize -> UINT16','uintsize',1,'p_uintsize','sintaxisJJ.py',63),
  ('uintsize -> UINT32','uintsize',1,'p_uintsize','sintaxisJJ.py',64),
  ('uintsize -> UINT64','uintsize',1,'p_uintsize','sintaxisJJ.py',65),
  ('uintsize -> UINT128','uintsize',1,'p_uintsize','sintaxisJJ.py',66),
  ('funcion -> FN ID LPAREN params RPAREN LLLAVE metodo RLLAVE','funcion',8,'p_funcion_sinreturn','sintaxisAB.py',65),
  ('impresion -> PRINTLN LPAREN IDSTRING RPAREN ENDCHAR','impresion',5,'p_impresion','sintaxisAB.py',68),
  ('strsize -> AMPERSAND COMILLA STATIC STR','strsize',4,'p_strsize','sintaxisJJ.py',70),
  ('strsize -> AMPERSAND STR','strsize',2,'p_strsize','sintaxisJJ.py',71),
  ('entrada -> IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN ENDCHAR','entrada',13,'p_entrada','sintaxisPR.py',70),
  ('entrada -> IO DOSDOBLEPUNTOS STDIN LPAREN RPAREN POINT READLINE LPAREN AMPERSAND MUT ID RPAREN POINT EXPECT LPAREN IDSTRING RPAREN ENDCHAR','entrada',18,'p_entrada','sintaxisPR.py',71),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintaxisJJ.py',75),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintaxisJJ.py',76),
  ('ifparams -> ifcondicion','ifparams',1,'p_ifparams','sintaxisJJ.py',84),
  ('ifparams -> boolean','ifparams',1,'p_ifparams','sintaxisJJ.py',85),
  ('ifparams -> ID','ifparams',1,'p_ifparams','sintaxisJJ.py',86),
  ('elseblock -> ifblock ELSE LLLAVE cuerpof RLLAVE','elseblock',5,'p_elseblock','sintaxisJJ.py',91),
  ('elseblock -> elseifblock ELSE LLLAVE cuerpof RLLAVE','elseblock',5,'p_elseblock','sintaxisJJ.py',92),
  ('elseifblock -> ifblock ELSE IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE','elseifblock',9,'p_elseifblock','sintaxisJJ.py',97),
  ('elseifblock -> ifblock ELSE IF ifparams LLLAVE cuerpof RLLAVE','elseifblock',7,'p_elseifblock','sintaxisJJ.py',98),
  ('ifblock -> IF LPAREN ifparams RPAREN LLLAVE cuerpof RLLAVE','ifblock',7,'p_ifblock','sintaxisJJ.py',103),
  ('ifblock -> IF ifparams LLLAVE cuerpof RLLAVE','ifblock',5,'p_ifblock','sintaxisJJ.py',104),
  ('ifcondicion -> comparacion','ifcondicion',1,'p_ifcondicion','sintaxisJJ.py',109),
  ('ifcondicion -> comparacion signoconect ifcondicion','ifcondicion',3,'p_ifcondicion','sintaxisJJ.py',110),
  ('ifcondicion -> LPAREN comparacion RPAREN','ifcondicion',3,'p_ifcondicion','sintaxisJJ.py',111),
  ('ifcondicion -> LPAREN comparacion RPAREN signoconect ifcondicion','ifcondicion',5,'p_ifcondicion','sintaxisJJ.py',112),
  ('ifcondicion -> LPAREN ifcondicion RPAREN','ifcondicion',3,'p_ifcondicion','sintaxisJJ.py',113),
  ('funcion -> FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof RETURN ifparams ENDCHAR RLLAVE','funcion',13,'p_funcion_retorno','sintaxisJJ.py',123),
  ('funcion -> FN ID LPAREN params RPAREN ARROWOPT datatype LLLAVE cuerpof ID RLLAVE','funcion',11,'p_funcion_returnimplicito','sintaxisJJ.py',128),
]
