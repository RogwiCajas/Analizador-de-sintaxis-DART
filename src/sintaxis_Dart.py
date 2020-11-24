 # Yacc example

import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from lex_Dart import tokens



def p_algoritmo(p): #regla padre, necesaria para llegar a todas 
    '''algoritmo : imprimir
                    | asignacion 
                    | expresion 
                    | comparacion
                    | sentenciaIf 
                    | sentenciaFOR
                    | sentenciaWhile
                    | empty
    '''


def p_asignacion(p):
    'asignacion : tipo VARIABLE IGUAL expresiones END'


##posibles asignaciones
def p_expresiones(p): #posible error, poner String
    '''expresiones : expresion
                    | comparacion
                    | BOOLEAN
                    | opstring
                    | indexacion
    '''

def p_strings(p):
    '''string : STRING
    '''

def p_operacion_strings(p):
    '''opstring : string 
                | VARIABLE
                | string MAS opstring
    '''

def p_imprimir(p):
    'imprimir : PRINT PIZQ expresiones PDER END'

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
                    | MOD
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
            | empty
            | VOID
    '''

def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''
##### estructura if
def p_sentenciaIf(p):
    'sentenciaIf : IF PIZQ comparacion PDER LIZQ algoritmo LDER varianteIf END'


def p_sentenciaelseif(p):
    '''varianteIf : ELSEIF PIZQ comparacion PDER LIZQ algoritmo LDER
                    | ELSE LIZQ algoritmo LDER
                    | ELSEIF PIZQ comparacion PDER LIZQ algoritmo LDER varianteIf
                    | empty
    '''
##### estructura for, for in

def p_setenciaFor(p):
    '''sentenciaFOR : FOR PIZQ parametros PDER LIZQ algoritmo LDER END
    '''

def p_contenidoFor(p):
    '''parametros : inicializacionFor END  comparacion END VARIABLE increDecre
                    | VARIABLE IN VARIABLE
    '''
def p_iniializacionFor(p):
    '''inicializacionFor : VARIABLE IGUAL ENTERO
                            | INT VARIABLE IGUAL ENTERO
                            | VAR VARIABLE IGUAL ENTERO
    '''
def p_increDecre(p):
    ''' increDecre : INCREMENTO
                    | DECREMENTO
    '''
##### estructura while, while..do

def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE PIZQ comparacion PDER LIZQ algoritmo LDER END
    '''

def p_sentenciaWhile_do(p):
    '''sentenciaWhile : DO LIZQ algoritmo LDER WHILE PIZQ comparacion PDER END
    '''
# indexacion
def p_indexacion(p):
    '''indexacion :  VARIABLE CIZQ  valor CDER  
    '''

def p_empty(p):
    'empty :'
    pass


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
'''
f=open("algoritmo.txt")
s = f.read()
print(s)
result = parser.parse(s)
print(result)
f.close()    
'''