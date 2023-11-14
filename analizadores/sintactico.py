# Yacc import
import ply.yacc as yacc
# Token map from the lexer
from analizadores.lexico import tokens

def p_sentencia(p):
    '''sentencia : bloques 
                | funcion
                '''
def p_bloques(p):
    '''bloques : impresion
                | ingreso
                | asignacion
                | estructura
                | declaracion
                '''

def p_estructura(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY asignacion RKEY'

def p_estructura_vacia(p):
    'estructura : TYPE IDENTIFICADOR STRUCT LKEY RKEY'

def p_def_funcion_con_parametros_con_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN parametros RPAREN tdato LKEY sentencia RETURN IDENTIFICADOR RKEY' 

def p_def_funcion_con_parametros_sin_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN parametros RPAREN LKEY sentencia RKEY'

def p_def_funcion_sin_parametros_con_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN RPAREN tdato LKEY sentencia RETURN IDENTIFICADOR RKEY'

def p_def_funcion_sin_parametros_sin_return(p):
    'funcion : FUNC IDENTIFICADOR LPAREN RPAREN LKEY sentencia RKEY'

def p_declaracionVariable(p):
    'declaracion : VAR IDENTIFICADOR tdato ASSIGN valor'

def p_declaracionVariable_vacia(p):
    'declaracion : VAR IDENTIFICADOR tdato'
                
def p_declaracionVariable_simple(p):
    '''declaracion : IDENTIFICADOR COLLON ASSIGN ENTERO
                | IDENTIFICADOR COLLON ASSIGN IDENTIFICADOR
                | IDENTIFICADOR COLLON ASSIGN BOOL
                | IDENTIFICADOR COLLON ASSIGN FLOTANTE
                '''
                
def p_declaracionVariable_estructura(p):
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
    '''valor : ENTERO
            | FLOTANTE
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
