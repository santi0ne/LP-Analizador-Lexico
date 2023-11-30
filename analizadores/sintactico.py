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
                | operaciones
                | est_datos
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
    '''declaracion : IDENTIFICADOR ASSIGNV valor
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
    '''tdato : INT32
             | INT64
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
    
def p_est_datos(p):
    '''est_datos : lista
                 | mapa
                 | conjunto
                 '''

def p_lista(p):
    '''lista : lista_vacia
             | lista_con_datos
             | lista_definida
             '''
    
def p_lista_vacia(p):
    'lista_vacia : VAR IDENTIFICADOR BRACKET tdato'

def p_lista_con_datos(p):
    'lista_con_datos : IDENTIFICADOR ASSIGNV BRACKET tdato LKEY valores RKEY'

def p_lista_definida(p):
    'lista_definida : IDENTIFICADOR ASSIGNV MAKE LPAREN BRACKET tdato COMA ENTERO COMA ENTERO RPAREN'

def p_mapa(p):
    '''mapa : mapa_vacio
            | mapa_con_datos
            '''

def p_mapa_vacio(p):
    'mapa_vacio : IDENTIFICADOR ASSIGNV MAKE LPAREN MAP LBRACKET tdato RBRACKET tdato RPAREN'

def p_mapa_con_datos(p):
    'mapa_con_datos : IDENTIFICADOR ASSIGNV MAP LBRACKET tdato RBRACKET tdato LKEY valores_mapa RKEY'

def p_valores_mapas(p):
    '''valores_mapa : valor_mapa
                    | valor_mapa COMA valores_mapa'''

def p_valor_mapa(p):
    'valor_mapa : dato COLLON dato'

def p_conjunto(p):
    '''conjunto : conjunto_con_mapa
                | conjunto_con_slice
                '''
    
def p_conjunto_con_mapa(p):
    '''conjunto_con_mapa : IDENTIFICADOR ASSIGNV MAKE LPAREN MAP LBRACKET tdato RBRACKET BOOL RPAREN'''

def p_conjunto_con_slice(p):
    '''conjunto_con_slice : IDENTIFICADOR ASSIGNV BRACKET tdato LKEY RKEY'''

def p_dato(p):
    '''dato : NUMERO
            | CADENA
            | BOOLEANO
            '''

# Jeremy Martinez
def p_operaciones(p):
    '''operaciones : suma
                    | resta
                    | producto
                    | division
                    | incremento
                    | decremento
                    '''

def p_suma(p):
    '''suma : NUMERO SUMA NUMERO
                | IDENTIFICADOR SUMA IDENTIFICADOR
                | IDENTIFICADOR SUMA NUMERO
            '''

def p_resta(p):
    '''resta : NUMERO RESTA NUMERO
                | IDENTIFICADOR RESTA IDENTIFICADOR
                | IDENTIFICADOR RESTA NUMERO
            '''
def p_producto(p):
    '''producto : NUMERO MULTIPLICACION NUMERO
                | IDENTIFICADOR MULTIPLICACION IDENTIFICADOR
                | IDENTIFICADOR MULTIPLICACION NUMERO
            '''

def p_division(p):
    '''division : NUMERO DIVISION NUMERO
                | IDENTIFICADOR DIVISION IDENTIFICADOR
                | IDENTIFICADOR DIVISION NUMERO
                '''
def p_incremento(p):
    '''incremento : IDENTIFICADOR INCREMENTO
                '''

def p_decremento(p):
    '''decremento : IDENTIFICADOR DECREMENTO
                '''