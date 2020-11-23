...
def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
print("Proyecto Analizador léxico :)") 



#fin de parte de Rogwi Cajas

#parte IsaacSolis
archivo = open('../codigoCajas.txt')
for linea in archivo:
    #print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break
