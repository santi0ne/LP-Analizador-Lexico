# Yacc import
import ply.yacc as yacc
# Token map from the lexer
from lexico import tokens

def p_sentencia(p):
    '''sentencia : impresion
                | asignacion
                | variable
                '''
                
def p_variable(p):
    'variable : VAR IDENTIFICADOR ASSIGN valor'

def p_asignacion(p):
    "asignacion : IDENTIFICADOR ASSIGN valores"


def p_impresion(p):
    "impresion : IMPRIMIR LPAREN valores RPAREN "

def p_impresion_sin_valor(p):
    'impresion : IMPRIMIR LPAREN RPAREN'

def p_valores(p):
    '''valores : valor
                | valor COMA valores
                '''
def p_valor(p):
    '''valor : ENTERO
            | FLOTANTE
            | STRING
            | BOOL
            | IDENTIFICADOR
            '''
    
def p_error(p):
    print("Error de sintaxis")

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
