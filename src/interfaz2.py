import tkinter
from tkinter import Tk
from RubyLexer import analizar
import SintacticoLex as sl

ventana = Tk()
ventana.geometry("800x640")


def analisisLexico(areaResultado, txt):
    areaResultado.delete("1.0", 'end-1c')

    linea = analizar(txt)
    areaResultado.insert(tkinter.INSERT, linea)


def analisisSintactico(areaResultado, txt):
    areaResultado.delete("1.0", 'end-1c')
    result = sl.parser.parse(txt)
    if sl.error[0] != "":
        areaResultado.insert(tkinter.INSERT, sl.error[0])
        sl.error[0] = ""

    else:
        areaResultado.insert(tkinter.INSERT, "Analisis Sintactico Correcto")


def analizadorSintac(codigo_text_area):
    areaResultado.delete("1.0", 'end-1c')

    txt = areaCodigo.get("1.0", 'end-1c')

    if txt != "":
        analisisSintactico(areaResultado, txt)


def analizadorLex(codigo_text_area):
    areaResultado.delete("1.0", 'end-1c')

    txt = areaCodigo.get("1.0", 'end-1c')

    if txt != "":
        analisisLexico(areaResultado, txt)


etiqueta = tkinter.Label(ventana, text="Analizador Ruby", font="Verdana", fg="blue")
etiqueta.place(x=50, y=10, width=150, height=50)

areaCodigo = tkinter.Text(ventana, height=7, width=30, )
areaCodigo.configure(relief="raised", borderwidth=2)
areaCodigo.place(x=10, y=50, width=400, height=150)

btn_lex = tkinter.Button(ventana, text=" Analizador Lexico ", padx=20, pady=20,
                         command=lambda: analizadorLex(areaCodigo))

btn_lex.place(x=10, y=200, width=150, height=80)

btn_sin = tkinter.Button(ventana, text="Analizador Sintactico", padx=20, pady=20,
                         command=lambda: analizadorSintac(areaCodigo))

btn_sin.place(x=230, y=200, width=160, height=80)

areaResultado = tkinter.Text(ventana, height=5, width=40)
areaResultado.configure(relief="raised", borderwidth=2)
areaResultado.place(x=10, y=300, width=400, height=150)

logo = tkinter.PhotoImage(file="ruby.png")

w = tkinter.Label(ventana,
                  image=logo).pack(side="right", padx=1)

ventana.mainloop()