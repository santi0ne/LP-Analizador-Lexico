import ply.yacc as yacc
from lexico import tokens
from sintactico import *

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('>>> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result != None:
       print(result)