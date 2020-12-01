import tkinter as tk
from sintaxis_Dart import analizarSintactico
from lex_Dart import analizarLexico


class Ventana:
    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        # Establecemos el tamaño de la raíz
        root.geometry("800x600")

        # Añadimos titulo

        self.titulo = tk.Label(root, text="Analizador Léxico y Sintáctico de Dart.")
        self.titulo.place(x=100, y=20)
        self.titulo.config(fg="blue",
                     font=("Verdana", 20))

        # Añadimos entrada

        self.Labelentrada = tk.Label(root, text="Ingrese su expresion:  ")
        self.Labelentrada.place(x=10, y=70)
        self.Labelentrada.config(fg="black",
                           font=("Verdana", 10))

        self.txt = tk.Entry(root, width = 100)
        self.txt.place(x=160,y=70)
        self.txt.focus()


        # Añadimos botones

        self.buttonLexico = tk.Button(root, text="Analizar Léxico", command=self.analizarLexco)
        self.buttonLexico.place(x=100, y=130)
        self.buttonLexico.config(fg="white",  # Foreground
                                  bg="blue",  # Background
                                  font=("Verdana", 16))

        self.buttonSintactico = tk.Button(root, text="Analizar Sintáctico", command=self.analizarSintactico)
        self.buttonSintactico.place(x=300, y=130)
        self.buttonSintactico.config(fg="white",  # Foreground
                                 bg="blue",  # Background
                                 font=("Verdana", 16))

        self.buttonLimpiar = tk.Button(root, text="Limpiar", command=self.limpiar, )
        self.buttonLimpiar.place(x=100, y=200)
        self.buttonLimpiar.config(fg="black",  # Foreground
                                  bg="white",  # Background
                                  font=("Verdana", 16))




        self.resultado = tk.Label(root,text= "Resultados",justify=tk.LEFT )
        self.resultado.place(x=10, y=250)
        self.resultado.config(fg="blue",
                              bg="white",
                              font=("Verdana", 15)
                              )



        # Definimos la función como un método de clase
    def analizarLexco(self):
        print("Se realizara un analizador léxico!")
        entrada= self.txt.get()
        resultados = analizarLexico(entrada)
        self.resultado['text'] = resultados


    def analizarSintactico(self):
        print("Se realizara un analizador sintáctico!")
        entrada = self.txt.get()
        resultados= analizarSintactico(entrada)
        self.resultado['text'] = resultados

    def limpiar(self):
        self.txt.delete(first=0, last=10000)
        self.resultado['text'] ="Resultados del Analizador"



# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
window = Ventana(win)
win.mainloop()