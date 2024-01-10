from tkinter import *
from tkinter import ttk 


def Operacion(event):
  dato = caja.get()
  dato =eval(dato)
  dato = str(dato)
  Limpiar()
  caja.insert(0,dato)

def Insertar(n):
    caja.insert("",n)

def Limpiar():
    caja.delete(0,END)

def borrar():
    b=caja.get()[:-1]
    Limpiar()
    caja.insert("",b)

tk=Tk()
caja= ttk.Entry(tk)
caja.grid(row=0,column=0,columnspan=4)
caja.bind("<Return>", Operacion)

linpiar= Button(tk,text="C",command=Limpiar)
linpiar.grid(row=1,column=0,columnspan=2, sticky=W + E)

borrar= Button(tk,text="DELETE",command=borrar)
borrar.grid(row=1,column=2,columnspan=2, sticky=E +  W)

bt_1= Button(tk,text="1",command=lambda: Insertar(n="1"))
bt_1.grid(row=2,column=0, columnspan=1, sticky=E +  W)

bt_2= Button(tk,text="2",command=lambda: Insertar(n="2"))
bt_2.grid(row=2,column=1, columnspan=1, sticky=E +  W)

bt_3= Button(tk,text="3",command=lambda: Insertar(n="3"))
bt_3.grid(row=2,column=2, columnspan=1, sticky=E +  W)

bt_suma= Button(tk,text="+",command=lambda: Insertar(n="+"))
bt_suma.grid(row=2,column=3, columnspan=1, sticky=E +  W)

bt_4= Button(tk,text="4",command=lambda: Insertar(n="4"))
bt_4.grid(row=3,column=0, columnspan=1, sticky=E +  W)

bt_5= Button(tk,text="5",command=lambda: Insertar(n="5"))
bt_5.grid(row=3,column=1, columnspan=1, sticky=E +  W)
bt_6= Button(tk,text="6",command=lambda: Insertar(n="6"))
bt_6.grid(row=3,column=2, columnspan=1, sticky=E +  W)

bt_resta= Button(tk,text="-",command=lambda: Insertar(n="-"))
bt_resta.grid(row=3,column=3, columnspan=1, sticky=E +  W)

bt_7= Button(tk,text="7",command=lambda: Insertar(n="7"))
bt_7.grid(row=4,column=0, columnspan=1, sticky=E +  W)
bt_8= Button(tk,text="8",command=lambda: Insertar(n="8"))
bt_8.grid(row=4,column=1, columnspan=1, sticky=E +  W)
bt_9= Button(tk,text="9",command=lambda: Insertar(n="9"))
bt_9.grid(row=4,column=2, columnspan=1, sticky=E +  W)

bt_divicion= Button(tk,text="/",command=lambda: Insertar(n="/"))
bt_divicion.grid(row=4,column=3, columnspan=1, sticky=E +  W)

bt_0= Button(tk,text="0",command=lambda: Insertar(n="0"))
bt_0.grid(row=5,column=0, columnspan=1, sticky=E +  W)

bt_punto= Button(tk,text=".",command=lambda: Insertar(n="."))
bt_punto.grid(row=5,column=1, columnspan=1, sticky=E +  W)



bt_igual= Button(tk,text="=",command= lambda: Operacion(""))
bt_igual.grid(row=5,column=2, columnspan=1, sticky=E +  W)

bt_multiplicacion= Button(tk,text="*",command=lambda: Insertar(n="*"))
bt_multiplicacion.grid(row=5,column=3, columnspan=1, sticky=E +  W)

tk.mainloop()

