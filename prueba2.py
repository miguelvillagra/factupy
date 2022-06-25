# import tkinter as tk


# def on_change(e):
#     print (e.widget.get())

# root = tk.Tk()

# e = tk.Entry(root)
# e.pack()    
# # Calling on_change when you press the return key
# e.bind("<Return>", on_change)  

# root.mainloop()




# import tkinter as tk

# root= tk.Tk()

# canvas1 = tk.Canvas(root, width = 400, height = 300)
# canvas1.pack()

# entry1 = tk.Entry (root) 
# canvas1.create_window(200, 140, window=entry1)

# def getSquareRoot ():  
#     x1 = entry1.get()
    
#     label1 = tk.Label(root, text= float(x1)**0.5)
#     canvas1.create_window(200, 230, window=label1)
    
# button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
# canvas1.create_window(200, 180, window=button1)

# root.mainloop()



from tkinter import *
from xml.etree.ElementTree import tostring
from CompraControlador import *
from nucleo import *
prueba = CompraControlador

clientee= Cliente("12345", "Miguel ANgel", "asu")

factura = prueba.relizar_factura(prueba, clientee)
def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label = Label(root, text = tostring(factura) )
    #this creates a new label to the GUI
    label.pack() 

root = Tk()

button = Button(root, text="Print Me", command=printSomething) 
button.pack()

root.mainloop()