import ply.lex as lex

##Palabras reservadas de dart
reserved = { 
    "if":"IF",
    "else": "ELSE",
    "for":"FOR",
    "while":"WHILE",
    "bool":"BOOL",
    "int":"INT",
    "double":"DOUBLE",
    "var":"VAR",
    "void":"VOID",
    "return": "RETURN",
    "in":"IN",
    "continue":"CONTINUE",
    "break": "BREAK"
}
## tokens

tokens = [
    
    "STRING",
    "END",
    "BOOLEAN",
    "VARIABLE",
    "IGUAL",
    "DIGUAL", 
    "DIF", 
    "PROD",
    "MOD",
    "MAYOR",
    "MENOR",
    "MAYORIG",
    "MENORIG",
    "ENTERO",
    "MAS",
    "INCREMENTO",
    "MENOS",
    "DECREMENTO",
    "DIV",
    "RESTA",
    "LIZQ",
    "LDER",
    "CIZQ",
    "CDER",
    "PIZQ",
    "PDER",
    "AND",
    "OR",
    "NEGACION",
    "COMA",
    "ELSEIF",
    "POINT"
    
] + list(reserved.values())

##especificacion de tokens

t_STRING=r"(\".*\")|(\'.*\')"
t_IGUAL= r"="
t_DIGUAL=r"=="
t_DIF= r"!="
t_PROD = r"\*"
t_MAS = r"\+"
t_INCREMENTO =r"\+\+"
t_MENOS = r"-"
t_DECREMENTO = r"--"
t_MOD = r"%"
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYORIG = r">="
t_MENORIG = r">="
t_ENTERO = r"\d+"
t_DIV=r"/"
t_RESTA=r"-"
t_CIZQ=r"\["
t_CDER=r"\]"
t_LIZQ=r"\{"
t_LDER=r"\}"
t_PIZQ=r"\("
t_PDER=r"\)"
t_END=r";"
t_AND=r"&&"
t_OR=r"\|\|"
t_NEGACION=r"!"
t_COMA=r","
t_POINT=r"\."

def t_ELSEIF(t):
    r"else\sif"
    t.type = reserved.get(t.value, 'ELSEIF')
    return t
def t_BOOLEAN(t):
    r"true|false"
    t.type = reserved.get(t.value, 'BOOLEAN')
    return t
def t_VARIABLE(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
# iGNORA CARACTERES
t_ignore = ' \t'
t_ignore_CM = r'//.*'
t_ignore_CM2 = r'/\*.*\*/'

def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
print("Mi primer analizador léxico :)")
#while True:
#   data = input(">> ")
#    analizar(data)
#    if len(data)==0:
#        break
archivo = open('codigo.txt')
for linea in archivo:
    #print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break