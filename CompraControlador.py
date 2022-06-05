
from http import client
from InterfazPasteleria import InterfazPasteleria
from nucleo import *

#   \
#Arreglar y agregar el ZODB
##Por el momento funcionan
#  1- Agreggar productos
#  2- Salir
#  Agregar productos: #  1-Pastel Gourmet #  3-Pastel Helado#  4-Finalizar compra
#y realizar factura sin datos de cliente

mi_lista = []  # array en donde guardamos los prodctos a comprar


class CompraControlador(object):
    """docstring for PasajeControlador"""

    def __init__(self):
        self.interfazPasteleria = InterfazPasteleria()

    def agregar_nuevo_producto(self):
        producto = input(
            "Agregar productos: \n 1-Pastel Gourmet \n 2-Pastel Economico \n 3-Pastel Helado \n 4-Finalizar compra \n 5-Salir")
        # pasteleria = Pasteleria

        self.interfazPasteleria.agregar_producto(
            lambda: print("Se selecciono la opcion " + producto))
        if producto == "1":

           print(
               "1- Pastel Gourmet. Introduzca la cantidad, precio y sabor. En ese orden:  \n ")

           # PastelGourmet(cantidad, precio, sabor)
           pastel_gourmet = PastelGourmet(input(), input(), input())
           mi_lista.append(pastel_gourmet)
           print(type(mi_lista[0]).__name__)

           print("La cantidad de pasteles en el carrito es de: " + str(len(mi_lista)))
           print("Se agrego un pastel al carrito con las siguientes caracteristicas:\n ")
           print("Tipo de pastel: " +
                 str(type(mi_lista[len(mi_lista)-1]).__name__))
           print("Cantidad: " + pastel_gourmet.cantidad_gourmet + "Precio: " +
                 pastel_gourmet.precio_gourmet + "Sabor: " + pastel_gourmet.sabor_gourmet)
           print("Otra forma de imprimir las cosas dentro\n\n")

        elif producto == "2":  # Faltaria implentar mas codigo para la opcion dos, pastel economico
            opcion2 = input('''Elegiste el numero 2, pastel economico.
				Introduzca opcion "a" para pastel pequeño o "b" para pastel mediano ''')

            if (opcion2.lower()) == "a":
                print('''Elegiste la opcion "A" de pastel economico pequeño.
				Introduzca sabor y precio''')
                pastel_economico_pequenho = PastelPequeño(input(), input())

                print(
                    "Se agrego un pastel al carrito con las siguientes caracteristicas:\n ")
                print("Sabor: " + pastel_economico_pequenho.sabor_pequenho + "\n" +
                      "Precio: " + pastel_economico_pequenho.precio_pequenho)

        elif producto == "3":
            print(
                "Elegiste el numero 3, pastel helado. \n Introduzca la cantidad, precio y sabor. En dicho orden")

            pastel_helado = PastelHelado(input(), input(), input())
            mi_lista.append(pastel_helado)

            print("La cantidad de pasteles en el carrito es de: " +
                  str(len(mi_lista)))
            print("Se agrego un pastel al carrito con las siguientes caracteristicas:\n ")
            print("Tipo de pastel: " +
                  str(type(mi_lista[len(mi_lista)-1]).__name__))
            #print(type(mi_lista[len(mi_lista)-1]).__name__)
            print("Cantidad: " + pastel_helado.cantidad_helado + "\n" +
                  "Precio: " + pastel_helado.precio_helado + "\n" + "Sabor: " + pastel_helado.sabor_helado)
        elif producto == "4":
            print("Se ha finalizado la compra \n")

            s_n = input(
                "Para proceder a realizar la factura, desea cargar los datos del cliente? \n S o N")
            if s_n.lower() == "s":
                #llamar a una funcion que cargue al cliente con sus productos y sus datos tributarios
                self.carga_datos_cliente()
                #llamar a una funcion que imprima la factura con los datos cargados y termina el programa
                quit()
            else:
                #cargar de forma anonima
                self.carga_datos_cliente_anonimo()
                self.relizar_factura()
                #llamar a una funcion que imprima la factura con los datos anonimos y termina el programa
                quit()

        elif producto == "0":
            quit()

    def menu_principal(self):
        choice = input(
            " Introduzca una opcion \n 1- Agregar productos \n 2- Salir")

        # self.interfazPasteleria.menu_principal_factupy(
        #     lambda: print("Hola usuario \n"))

        while choice != "2":
            self.agregar_nuevo_producto()
        else:
           print("Gracias por usar FactuPy")

    def carga_datos_cliente(self):
        print(
            "Introduzca los datos del cliente. \n Cedula, nombre y direccion. En ese orden")
        cliente = Cliente(input(), input(), input())
        return cliente

    def carga_datos_cliente_anonimo(self):
        print(
            "Introduzca los datos del cliente. \n Cedula, nombre y direccion. En ese orden")
        cliente = Cliente(123456789, "Sin nombre", "Sin direccion")
        return cliente

    def relizar_factura(self):
        total = 0
        print("\n \n \n")
        print("Cantidad------Producto/sabor-------Precio------- IVA Total")

        for x in range(len(mi_lista)):
            iva = 0.1  # se debe multiplicar al precio de cada producto

            #implementar que imprima datos del cliente

            #aca imprime los productos en total
            if str(type(mi_lista[len(mi_lista)-1]).__name__) == "PastelGourmet":

                print(str(mi_lista[x].cantidad_gourmet) + "---Pastel Gourmet/" + str(mi_lista[x].sabor_gourmet) +
                      "---" + str(mi_lista[x].precio_gourmet) + "---" + str(mi_lista[x].precio_gourmet))
                print("\n")
                #Aca faltaria implementar condiciones para que imprima otro tipo de productos con la factura
                #solo funciona con pastel gourmet por el momento
            # elif == "PastelEconomico":
            #     pass
            # elif == "PastelHelado":
            #     pass
