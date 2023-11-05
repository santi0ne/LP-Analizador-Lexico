# ANALIZADOR LEXICO PARA GO

# Documentación: https://www.dabeaz.com/ply/ply.html

import ply.lex as lex

# Palabras Reservadas
reserved = {
   'var':'VAR'
}

# Secuencia de tokens
tokens = (
    'IDENTIFICADOR',
)+tuple(reserved.values())

# Expresiones Regulares simples para símbolos

# Expresiones Regulares para números y variables, incluye cast
def t_IDENTIFICADOR(t):
    r'[a-z_]\w*'
    t.type = reserved.get(t.value,'IDENTIFICADOR')
    return t

# Expresión regular para reconocer saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios, tabulaciones
t_ignore  = ' \t'

# Manejo de errores
def t_error(t):
  print(f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}")
  t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()

# Código para analizar
code = "var 781 piloso"

# Enviando el código
lexer.input(code)

# Tokenizar
for token in lexer:
  print(token)