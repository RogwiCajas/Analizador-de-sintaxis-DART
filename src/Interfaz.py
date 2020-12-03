import tkinter as tk
from sintaxis_Dart import analizarSintactico
from lex_Dart import analizarLexico


class Ventana:
    def NuevaVentana(self, nuevaventana):
        nuevaventana.geometry("800x600")


    # Le pasamos el componente raíz al constructor
    def __init__(self, root):
        # Establecemos el tamaño de la raíz
        root.geometry("800x400")

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




        # Definimos la función como un método de clase
    def analizarLexco(self):
        entrada= self.txt.get()
        resultados = analizarLexico(entrada)
        if resultados=="" :
            NueVentana("Error, no se reconocio ningun token")

        else:
            NueVentana(resultados)


    def analizarSintactico(self):
        print("Se realizara un analizador sintáctico!")
        entrada = self.txt.get()
        resultados,error= analizarSintactico(entrada)
        NueVentana(resultados + str(error))

    def limpiar(self):
        self.txt.delete(first=0, last=10000)

def NueVentana(resultados):
    toplevel = tk.Toplevel(width = 100)
    container = tk.Frame(toplevel)
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    labelresult = tk.Label(scrollable_frame, text=resultados, justify=tk.LEFT)
    labelresult.pack()
    labelresult.config(fg="blue",
                       bg="white",
                       font=("Verdana", 12)
                       )


    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")




# Creamos la aplicación, la ventana e iniciamos el bucle
win = tk.Tk()
window = Ventana(win)
win.mainloop()