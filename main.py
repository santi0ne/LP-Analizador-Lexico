import ply.yacc as yacc
from analizadores.lexico import *
from analizadores.sintactico import *
from pruebas.pruebas_sin import *

# Build the parser
parser = yacc.yacc()

'''
code= test_if()
result = parser.parse(code)
if result != None:
    print(result)
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

