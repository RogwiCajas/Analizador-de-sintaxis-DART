 # Yacc example

import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from lex_Dart import tokens



def p_algoritmo(p): #regla padre, necesaria para llegar a todas 
    '''algoritmo : imprimir END
                    | asignacion END
                    | expresion END
                    | comparacion
                    | sentenciaIf END
    '''

def p_sentenciaIf(p):
    'sentenciaIf : IF PIZQ comparacion PDER LIZQ algoritmo  LDER'

def p_asignacion(p):
    'asignacion : tipo VARIABLE IGUAL expresion'

def p_imprimir(p):
    'imprimir : PRINT PIZQ expresion PDER'

def p_expresion(p):
    '''expresion : valor
    '''
def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorMat(p):
    '''operadorMat : MAS 
                    | RESTA
                    | PROD
                    | DIV
    '''
def p_operadorComp(p):
    '''operadorComp : MAYOR 
                    | MENOR
                    | MAYORIG
                    | MENORIG
                    | DIGUAL
                    | DIF
    '''
def p_tipo(p):
    '''tipo : VAR
            | INT
            | BOOL
            | DOUBLE
    '''
def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''




# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)