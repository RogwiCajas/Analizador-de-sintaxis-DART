 # Yacc example

import ply.yacc as yacc
 
 # Get the token map from the lexer.  This is required.
from lex_Dart import tokens
#flag
reglas=[]

def p_codigo(p): #Rogwi Cajas
    '''codigo : algoritmo
                | algoritmo codigo

    '''
    

def p_algoritmo(p): #regla padre, necesaria para llegar a todas 
    '''algoritmo : imprimir
                    | asignacion 
                    | expresion END
                    | comparacion END
                    | sentenciaIf 
                    | sentenciaFOR
                    | sentenciaWhile
                    | input
                    | funciones
                    | expresionSinRetorno
    '''
    
def p_funciones(p):
    '''funciones : tipo VARIABLE PIZQ parametros PDER LIZQ codigo RETURN expresion END LDER
                | VOID VARIABLE PIZQ parametros PDER LIZQ codigo   LDER
    '''
    

def p_asignacion(p): #Rogwi Cajas
    '''asignacion : tipo VARIABLE IGUAL expresiones END
                    | VARIABLE IGUAL expresiones END
    '''
    


def p_expresionSinRetorno(p): #Isaac Solis
    '''expresionSinRetorno : funcionStructura END
                           | funcionStructura
    '''
    

def p_funcionStructura(p): #funciones de listas y conjuntos
    '''funcionStructura : first
                        | last
                        | length
                        | remove
                        | add
    '''
    
def p_parametros(p):
    '''parametros : empty 
                  | tipo VARIABLE
                  | tipo VARIABLE COMA  parametros
    '''
    
##posibles asignaciones #Rogwi Cajas e isaac solis
def p_strings(p):
    '''string : STRING
    '''
    

def p_expresiones(p): #p, poner String
    '''expresiones : expresion
                    | comparacion
                    | BOOLEAN
                    | opstring
                    | indexacion
                    | lista
                    | conjuntos
                    | first
                    | last
                    | length
                    | remove
                    | add
                    | slice
                    | opLogicas
    '''

def p_operacion_strings(p): #Rogwi Cajas
    '''opstring : string 
                | VARIABLE
                | string MAS opstring
                | VARIABLE MAS opstring
    '''

def p_imprimir(p):
    'imprimir : PRINT PIZQ opstring PDER END'


def p_input(p):
    'input : tipo VARIABLE IGUAL INPUT PIZQ PDER END'

def p_expresion(p):
    '''expresion : valor
    '''

def p_lista(p):
    '''lista : CIZQ elementos CDER
    '''

def p_first(p):
    '''first : VARIABLE POINT FIRST PIZQ PDER
    '''

def p_last(p):
    '''last : VARIABLE POINT LAST PIZQ PDER
    '''

def p_length(p):
    '''length : VARIABLE POINT LEN PIZQ PDER
    '''

def p_add(p):
    '''add : VARIABLE POINT ADD PIZQ valor PDER
    '''

def p_slice(p):
    '''slice : VARIABLE POINT SLICE PIZQ valor COMA valor PDER
    '''


def p_remove(p):
    '''remove : VARIABLE POINT REMOVE PIZQ valor PDER
    '''
def p_conjuntos(p):
    '''conjuntos : LIZQ elementos LDER
    '''

def p_elementos(p):
    '''elementos : valor
                 | valor COMA elementos
    '''
def p_operaciones_logicas(p):
    '''opLogicas :    terminoLogico
                    | terminoLogico operadorLog terminoLogico
                    | terminoLogico operadorLog terminoLogico operadorLog opLogicas
    '''
def p_termino_logico(p):
    ''' terminoLogico : VARIABLE
                        | BOOLEAN
                        | PIZQ comparacion PDER
    '''


def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'


def p_comparacion(p):
    'comparacion : expresion operadorComp expresion'

def p_operadorLog(p):
    '''operadorLog : AND
                    | OR
    '''
def p_operadorMat(p): #Rogwi Cajas
    '''operadorMat : MAS 
                    | RESTA
                    | PROD
                    | DIV
                    | MOD
    '''

def p_operadorComp(p): #Rogwi Cajas
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
            | VOID
            | STR
    '''

def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''

##### estructura if Rogwi Cajas
def p_sentenciaIf(p):
    '''sentenciaIf : IF PIZQ comparacion PDER LIZQ algoritmo LDER varianteIf
                    | IF PIZQ opLogicas PDER LIZQ algoritmo LDER varianteIf
    '''


def p_sentenciaelseif(p):
    '''varianteIf : ELSEIF PIZQ comparacion PDER LIZQ algoritmo LDER
                    | ELSEIF PIZQ opLogicas PDER LIZQ algoritmo LDER
                    | ELSE LIZQ algoritmo LDER
                    | ELSEIF PIZQ comparacion PDER LIZQ algoritmo LDER varianteIf
                    | ELSEIF PIZQ opLogicas PDER LIZQ algoritmo LDER varianteIf
                    | empty
    '''
##### estructura for, for in Rogwi Cajas

def p_setenciaFor(p):
    '''sentenciaFOR : FOR PIZQ parametrosF PDER LIZQ algoritmo LDER
    '''

def p_contenidoFor(p):
    '''parametrosF : inicializacionFor END  comparacion END VARIABLE increDecre
                    | inicializacionFor END  opLogicas END VARIABLE increDecre
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
##### estructura while, while..do Rogwi Cajas

def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE PIZQ comparacion PDER LIZQ algoritmo LDER
                        | WHILE PIZQ opLogicas PDER LIZQ algoritmo LDER
    '''

def p_sentenciaWhile_do(p):
    '''sentenciaWhile : DO LIZQ algoritmo LDER WHILE PIZQ comparacion PDER END
                        | DO LIZQ algoritmo LDER WHILE PIZQ opLogicas PDER END
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
    if p is not None:
        reglas.append("Syntax Error: \n '%s' \n, l= %s c= %s"%(p.value,p.lineano,p.lexpos))

    else:
        print("Syntax Error!!")
        reglas.append("Syntax Error")#añade el error a el arreglo


# Build the parser
parser = yacc.yacc()

def analizarSintactico(s):
    reglas.clear()#limpio los errores de analisis pasados
    print(s)
    result = str(parser.parse(s))
    print(result)
    
    return result,reglas

'''
f=open("codigoCajas.txt")
s = f.read()
print(s)
result = parser.parse(s)
print(result)
f.close() '''   

