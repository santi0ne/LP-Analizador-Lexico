import ply.yacc as yacc

from analizadores.lexico import *
from analizadores.sintactico import *
from pruebas.pruebas_sin import *
from pruebas.pruebas_lex import *
import sys
import tkinter as tk
from tkinter import scrolledtext

#Aqui probamos los algoritmos del sintactico
# code= test_division()
# result = parser.parse(code)
# if result != None:
#    print(result)

# Construye el lexer y parser
lexer = lex.lex()
parser = yacc.yacc()

# Código para analizar
# code = test_mayorQue()
# Enviando el código
# lexer.input(code)

# Tokenizar
# for token in lexer:
#    print(token)



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
class StdoutRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(tk.END, text)
        self.widget.see(tk.END)


def execute_parsing():
    code = code_input.get("1.0", tk.END)  # Obtener el código del text area
    result_text.delete("1.0", tk.END)  # Limpiar la salida anterior
    
    sys.stdout = StdoutRedirector(result_text)
    lexer = lex.lex()
    parser = yacc.yacc()

    '''
    result = parser.parse(code)
    if result is not None:
        print(result)'''
    result = parser.parse(code)
    if result is not None:
        print(result)
    else:
        print("No hubo errores durante el análisis sintáctico.")



# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Analizador Sintáctico GO")
'''
# Frame principal
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)



# Text area para ingresar el código
code_input = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
code_input.pack(expand=True, fill=tk.BOTH)

# Panel tipo shell para mostrar la salida
result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
result_text.pack(expand=True, fill=tk.BOTH)


# Botón "Run" para ejecutar el análisis sintáctico
run_button = tk.Button(root, text="Run", command=execute_parsing)
run_button.pack()
'''
# Frame principal
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)


# Text area para ingresar el código
code_input = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
code_input.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Panel tipo shell para mostrar la salida
result_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD)
result_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

# Botón "Run" para ejecutar el análisis sintáctico
run_button = tk.Button(main_frame, text="Run", command=execute_parsing)
run_button.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

root.mainloop()
