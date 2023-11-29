import ply.yacc as yacc

from analizadores.lexico import *
from analizadores.sintactico import *
from pruebas.pruebas_sin import *
from pruebas.pruebas_lex import *

# Build the parser
# parser = yacc.yacc()

#Aqui probamos los algoritmos del sintactico
# code= test_division()
# result = parser.parse(code)
# if result != None:
#    print(result)

# Construye el lexer
lexer = lex.lex()

# Código para analizar
code = test_mayorQue()
# Enviando el código
lexer.input(code)

# Tokenizar
for token in lexer:
    print(token)



#Aqui probamos el yac por la terminal
'''
while True:
   try:
       s = input('>>> ')
       if s == "exit": break
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result != None:
       print(result)
'''