# Yacc import
import ply.yacc as yacc
# Token map from the lexer
from analizadores.lexico import tokens

def p_sentencia(p):
    '''sentencia : bloques 
                | estructura
                | funcion
                '''
def p_bloques(p):
    '''bloques : bloque
               | bloque SALTO bloques
               '''

def p_bloque(p):
    '''bloque : impresion
                | ingreso
                | asignacion
                | declaracion
                | condiciones
                | clausula_if
                '''

def p_estructura(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY sentencia RKEY'

def p_estructura_vacia(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY RKEY'

def p_funcion_con_parametros_con_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN parametros RPAREN tdato LKEY bloques RETURN IDENTIFICADOR RKEY' 

def p_funcion_con_parametros_sin_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN parametros RPAREN LKEY bloques RKEY'

def p_funcion_sin_parametros_con_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN RPAREN tdato LKEY bloques RETURN IDENTIFICADOR RKEY'

def p_funcion_sin_parametros_sin_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN RPAREN LKEY bloques RKEY'

def p_declaracion_variable(p):
    'declaracion : VAR IDENTIFICADOR tdato ASSIGN valor'

def p_declaracion_variable_vacia(p):
    'declaracion : VAR IDENTIFICADOR tdato'
                
def p_declaracion_variable_simple(p):
    '''declaracion : IDENTIFICADOR COLLON ASSIGN valor
                '''
                
def p_declaracion_variable_estructura(p):
    'declaracion : IDENTIFICADOR tdato'

def p_asignacion(p):
    'asignacion : IDENTIFICADOR ASSIGN valores'

def p_impresion(p):
    'impresion : IMPRIMIR LPAREN valores RPAREN'

def p_impresion_sin_valor(p):
    'impresion : IMPRIMIR LPAREN RPAREN'

def p_ingreso(p):
    'ingreso : INGRESO LPAREN valores RPAREN'

def p_ingreso_sin_valor(p):
    'ingreso : INGRESO LPAREN RPAREN'

def p_valores(p):
    '''valores : valor
                | valor COMA valores
                '''
    
def p_valor(p):
    '''valor : NUMERO
            | CADENA
            | BOOLEANO
            | IDENTIFICADOR
            '''
    
def p_parametros(p):
    '''parametros : parametro
                  | parametro COMA parametros
                  '''

def p_parametro(p):
    'parametro : IDENTIFICADOR tdato'

def p_tdatos(p):
    '''tdato : INT
             | STRING
             | FLOAT32
             | FLOAT64
             | BOOL
             '''
    
def p_error(p):
    print("Error de sintaxis")

# AVANCE 3

# Johnny Santiago Rodriguez Salinas

def p_clausula_if(p):
    'clausula_if : IF condiciones LKEY bloques RKEY'

def p_condiciones(p):
    '''condiciones : condicion
                   | condicion logico condiciones 
                   '''

def p_condicion(p):
    'condicion : IDENTIFICADOR relacionales NUMERO'

def p_logico(p):
    '''logico : AND
              | OR
              | NOT'''

def p_relacionales(p):
    '''relacionales : MAYORQUE        
                    | MENORQUE         
                    | MAYORIGUALQUE   
                    | MENORIGUALQUE                
                    | IGUALQUE         
                    | DIFERENTEQUE    
    '''

def p_numero(p):
    '''NUMERO : ENTERO
              | FLOTANTE
              '''
