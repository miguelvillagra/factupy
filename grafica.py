import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.messagebox
from turtle import heading
from CompraControlador import *
from nucleo import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
#controlador = CompraControlador()



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.subtitle_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, AgregarProductos, PastelGourmet, FinalizarCompra, PastelEconomico, PastelHelado, 
        PastelEconomicoPequeño, PastelEconomicoMediano, CargarDatosFactura, MostrarFactura):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
############################   ############################ ############################  

 

def salir():
   tkinter.messagebox.showinfo( "", "Gracias por usar FactuPy, hasta luego!")
   quit()


############################ ############################ ############################ ############################ 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#DCD7C9')
        self.controller = controller

        controller.title('FactuPy')
        controller.state('zoomed')
        controller.iconphoto(False, tk.PhotoImage(file='/Users/miguelvillagra/Desktop/proyecto/factupy/file.png'))

        heading_label1= tk.Label(self, text='FactuPy', font=('Helvetica',45,'bold'), foreground='#2C3639', background='#DCD7C9')
        heading_label1.pack( pady=25)

        space_label= tk.Label(self, height='4', background='#DCD7C9')
        space_label.pack()

        welcome_label= tk.Label(self, 
            text="Bienvenido a FactuPy. \nHaga clic a una opción", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        welcome_label.pack(pady=15)

       

        button1 = tk.Button(self, text="Agregar productos",
                            command=lambda: controller.show_frame("AgregarProductos"))
        button1.pack()
        
        boton_salir = tkinter.Button(self, text ="Salir", command = salir)
        boton_salir.pack()

        

class AgregarProductos(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background='#DCD7C9')
        self.controller = controller

        option_label = tk.Label(self, 
            text="Agregar productos. \nEliga una opción:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        

        button1 = tk.Button(self, text="Pastel Gourmet",
                           command=lambda: controller.show_frame("PastelGourmet"))
        button1.pack()
        button2 = tk.Button(self, text="Pastel Economico",
                           command=lambda: controller.show_frame("PastelEconomico"))
        button2.pack()
        button3 = tk.Button(self, text="Pastel Helado",
                           command=lambda: controller.show_frame("PastelHelado"))
        button3.pack()
        button4 = tk.Button(self, text="Finalizar compra",
                           command=lambda: controller.show_frame("FinalizarCompra"))
        button4.pack()

        button5 = tk.Button(self, text="Volver al inicio",
                           command=lambda: controller.show_frame("StartPage"))
        button5.pack()

class PastelGourmet (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Pastel gourmet. \n", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        #Acá introduce la cantidad
        amount_label = tk.Label(self, 
            text="Introduzca la cantidad:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        amount_label.pack(pady=15)
        amount= tk.IntVar()
        amount_entry_box= tk.Entry(
            self,
            textvariable=amount,
            font=('Helvetica',20,'bold'),
            width=15
        )
        amount_entry_box.pack(ipady=7)

        def add_amount():
            tkinter.messagebox.showinfo( "", "Se agrego la cantidad de pasteles")
        
        enter_button1= tk.Button(
            self,
            text='Enter',
            command=add_amount,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button1.pack(pady=10)



        #Aca introduce el precio
        price_label = tk.Label(self, 
            text="Introduzca el precio:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        price_label.pack(pady=15)

        
        price= tk.IntVar()
        price_entry_box= tk.Entry(
            self,
            textvariable=price,
            font=('Helvetica',20,'bold'),
            width=15
        )
        price_entry_box.pack(ipady=7)

        def add_price():
            tkinter.messagebox.showinfo( "", "Se agrego el precio del pastel")
        enter_button2= tk.Button(
            self,
            text='Enter',
            command=add_price,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button2.pack(pady=10)
        
        #Aca introduce el sabor
        flavor_label = tk.Label(self, 
            text="Introduzca el sabor:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        flavor_label.pack(pady=15)

        
        flavor= tk.StringVar()
        flavor_entry_box= tk.Entry(
            self,
            textvariable=flavor,
            font=('Helvetica',20,'bold'),
            width=15
        )
        flavor_entry_box.pack(ipady=7)

        def add_flavor():
            tkinter.messagebox.showinfo( "", "Se agrego el sabor del pastel")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_flavor,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)


        #Boton para volver atras
        button = tk.Button(self, text="Atrás",
                           command=lambda: controller.show_frame("AgregarProductos"))
        button.pack()

class PastelEconomico (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Pastel economico. \n", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        button1 = tk.Button(self, text="Pequeño",
                           command=lambda: controller.show_frame("PastelEconomicoPequeño"))
        button1.pack()
        button2 = tk.Button(self, text="Mediano",
                           command=lambda: controller.show_frame("PastelEconomicoMediano"))
        button2.pack()

         #Boton para volver atras
        button = tk.Button(self, text="Atrás",
                           command=lambda: controller.show_frame("AgregarProductos"))
        button.pack()

class PastelEconomicoPequeño (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Pastel economico pequeño. \n", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        #Acá introduce la cantidad
        amount_label = tk.Label(self, 
            text="Introduzca la cantidad:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        amount_label.pack(pady=15)
        amount= tk.IntVar()
        amount_entry_box= tk.Entry(
            self,
            textvariable=amount,
            font=('Helvetica',20,'bold'),
            width=15
        )
        amount_entry_box.pack(ipady=7)

        def add_amount():
            tkinter.messagebox.showinfo( "", "Se agrego la cantidad de pasteles")
        
        enter_button1= tk.Button(
            self,
            text='Enter',
            command=add_amount,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button1.pack(pady=10)



        #Aca introduce el precio
        price_label = tk.Label(self, 
            text="Introduzca el precio:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        price_label.pack(pady=15)

        
        price= tk.IntVar()
        price_entry_box= tk.Entry(
            self,
            textvariable=price,
            font=('Helvetica',20,'bold'),
            width=15
        )
        price_entry_box.pack(ipady=7)

        def add_price():
            tkinter.messagebox.showinfo( "", "Se agrego el precio del pastel")
        enter_button2= tk.Button(
            self,
            text='Enter',
            command=add_price,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button2.pack(pady=10)
        
        #Aca introduce el sabor
        flavor_label = tk.Label(self, 
            text="Introduzca el sabor:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        flavor_label.pack(pady=15)

        
        flavor= tk.StringVar()
        flavor_entry_box= tk.Entry(
            self,
            textvariable=flavor,
            font=('Helvetica',20,'bold'),
            width=15
        )
        flavor_entry_box.pack(ipady=7)

        def add_flavor():
            tkinter.messagebox.showinfo( "", "Se agrego el sabor del pastel")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_flavor,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

         #Boton para volver atras
        button = tk.Button(self, text="Atrás",
                           command=lambda: controller.show_frame("AgregarProductos"))
        button.pack()

class PastelEconomicoMediano (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Pastel economico mediano. \n", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        #Acá introduce la cantidad
        amount_label = tk.Label(self, 
            text="Introduzca la cantidad:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        amount_label.pack(pady=15)
        amount= tk.IntVar()
        amount_entry_box= tk.Entry(
            self,
            textvariable=amount,
            font=('Helvetica',20,'bold'),
            width=15
        )
        amount_entry_box.pack(ipady=7)

        def add_amount():
            tkinter.messagebox.showinfo( "", "Se agrego la cantidad de pasteles")
        
        enter_button1= tk.Button(
            self,
            text='Enter',
            command=add_amount,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button1.pack(pady=10)



        #Aca introduce el precio
        price_label = tk.Label(self, 
            text="Introduzca el precio:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        price_label.pack(pady=15)

        
        price= tk.IntVar()
        price_entry_box= tk.Entry(
            self,
            textvariable=price,
            font=('Helvetica',20,'bold'),
            width=15
        )
        price_entry_box.pack(ipady=7)

        def add_price():
            tkinter.messagebox.showinfo( "", "Se agrego el precio del pastel")
        enter_button2= tk.Button(
            self,
            text='Enter',
            command=add_price,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button2.pack(pady=10)
        
        #Aca introduce el sabor
        flavor_label = tk.Label(self, 
            text="Introduzca el sabor:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        flavor_label.pack(pady=15)

        
        flavor= tk.StringVar()
        flavor_entry_box= tk.Entry(
            self,
            textvariable=flavor,
            font=('Helvetica',20,'bold'),
            width=15
        )
        flavor_entry_box.pack(ipady=7)

        def add_flavor():
            tkinter.messagebox.showinfo( "", "Se agrego el sabor del pastel")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_flavor,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

         #Boton para volver atras
        button = tk.Button(self, text="Atrás",
                           command=lambda: controller.show_frame("AgregarProductos"))
        button.pack()

        

class PastelHelado (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Pastel Helado. \n", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)

        #Acá introduce la cantidad
        amount_label = tk.Label(self, 
            text="Introduzca la cantidad:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        amount_label.pack(pady=15)
        amount= tk.IntVar()
        amount_entry_box= tk.Entry(
            self,
            textvariable=amount,
            font=('Helvetica',20,'bold'),
            width=15
        )
        amount_entry_box.pack(ipady=7)

        def add_amount():
            tkinter.messagebox.showinfo( "", "Se agrego la cantidad de pasteles")
        
        enter_button1= tk.Button(
            self,
            text='Enter',
            command=add_amount,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button1.pack(pady=10)



        #Aca introduce el precio
        price_label = tk.Label(self, 
            text="Introduzca el precio:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        price_label.pack(pady=15)

        
        price= tk.IntVar()
        price_entry_box= tk.Entry(
            self,
            textvariable=price,
            font=('Helvetica',20,'bold'),
            width=15
        )
        price_entry_box.pack(ipady=7)

        def add_price():
            tkinter.messagebox.showinfo( "", "Se agrego el precio del pastel")
        enter_button2= tk.Button(
            self,
            text='Enter',
            command=add_price,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button2.pack(pady=10)
        
        #Aca introduce el sabor
        flavor_label = tk.Label(self, 
            text="Introduzca el sabor:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        flavor_label.pack(pady=15)

        
        flavor= tk.StringVar()
        flavor_entry_box= tk.Entry(
            self,
            textvariable=flavor,
            font=('Helvetica',20,'bold'),
            width=15
        )
        flavor_entry_box.pack(ipady=7)

        def add_flavor():
            tkinter.messagebox.showinfo( "", "Se agrego el sabor del pastel")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_flavor,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

         #Boton para volver atras
        button = tk.Button(self, text="Atrás",
                           command=lambda: controller.show_frame("AgregarProductos"))
        button.pack()


class FinalizarCompra (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Se ha finalizado la compra. \nPara proceder a realizar la factura, desea cargar los datos del cliente?", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)


        button1 = tk.Button(self, text="Si",
                            command=lambda: controller.show_frame("CargarDatosFactura"))
        button1.pack()
        button2 = tk.Button(self, text="No",
                            command=lambda: controller.show_frame("MostrarFactura"))
        button2.pack()
        # button = tk.Button(self, text="Volver al inicio",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()
    
    
class CargarDatosFactura (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Introduzca los datos del cliente.", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)


       #Aca introducen los datos correspondientes

       #Nombre y apellido
        name_label = tk.Label(self, 
            text="Introduzca el nombre y apellido:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        name_label.pack(pady=15)

        
        name= tk.StringVar()
        name_entry_box= tk.Entry(
            self,
            textvariable=name,
            font=('Helvetica',20,'bold'),
            width=15
        )
        name_entry_box.pack(ipady=7)

        def add_name():
            tkinter.messagebox.showinfo( "", "Se agregó el nombre y apellido del cliente")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_name,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

        #cedula de identidad o RUC
        ruc_label = tk.Label(self, 
            text="Introduzca el RUC o cedula de identidad:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        ruc_label.pack(pady=15)

        
        ruc= tk.StringVar()
        ruc_entry_box= tk.Entry(
            self,
            textvariable=ruc,
            font=('Helvetica',20,'bold'),
            width=15
        )
        ruc_entry_box.pack(ipady=7)

        def add_ruc():
            tkinter.messagebox.showinfo( "", "Se agregó el RUC/CI del cliente")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_ruc,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

        #direccion
        adress_label = tk.Label(self, 
            text="Introduzca la dirección/locación del cliente:", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#A27B5C'
        )
        adress_label.pack(pady=15)

        
        adress= tk.StringVar()
        adress_entry_box= tk.Entry(
            self,
            textvariable=adress,
            font=('Helvetica',20,'bold'),
            width=15
        )
        adress_entry_box.pack(ipady=7)

        def add_adress():
            tkinter.messagebox.showinfo( "", "Se agregó la dirección del cliente")

       
        enter_button3= tk.Button(
            self,
            text='Enter',
            command=add_adress,
            relief='raised',
            borderwidth=3,
            width=5,
            height=2
        )
        enter_button3.pack(pady=10)

        button = tk.Button(self, text="Listo",
                           command=lambda: controller.show_frame("MostrarFactura"))
        button.pack()

   
class MostrarFactura (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#DCD7C9')
        self.controller = controller
        option_label = tk.Label(self, 
            text="Aca se muestra la factura", 
            font=('Helvetica',20,'bold'),
            bg='#DCD7C9',
            foreground='#3F4E4F')
        option_label.pack(pady=25)
        boton_salir = tkinter.Button(self, text ="Salir", command = salir)
        boton_salir.pack()


        
    
    







if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()