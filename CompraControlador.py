
from http import client
from InterfazPasteleria import InterfazPasteleria
from nucleo import *
import math

#   \
# Arreglar y agregar el ZODB
# Por el momento funcionan
#  1- Agreggar productos
#  2- Salir
#  Agregar productos: #  1-Pastel Gourmet #  3-Pastel Helado#  4-Finalizar compra
# y realizar factura sin datos de cliente

mi_lista = []  # array en donde guardamos los pedidos a realizar
empresa = EmpresaGastronómica(
    "Ceci gross pastelería", "Mcal Lopez/José Vinuales")


class CompraControlador(object):
    """docstring for PasajeControlador """

    def __init__(self):
        self.interfazPasteleria = InterfazPasteleria()

    def agregar_nuevo_producto(self):
        producto = input(
            "Agregar productos: \n 1-Pastel Gourmet \n 2-Pastel Economico \n 3-Pastel Helado \n 4-Finalizar compra \n 5-Salir \n")
        # pasteleria = Pasteleria

        self.interfazPasteleria.agregar_producto(
            lambda: print("\nSe selecciono la opcion: " + producto))
        if producto == "1":

            print(
                "1- Pastel Gourmet. Introduzca la cantidad, precio y sabor. En ese orden:  \n ")

            # PastelGourmet(cantidad, precio, sabor)
            pastel_gourmet = PastelGourmet(input(), input(), input())
            mi_lista.append(pastel_gourmet)
            #print(type(mi_lista[0]).__name__)

            print("\nLa cantidad de pedidos en el carrito es de: " +
                  str(len(mi_lista)))
            print("Se agrego un pastel al carrito con las siguientes caracteristicas: ")
            print("Tipo de pastel: " +
                  str(type(mi_lista[len(mi_lista)-1]).__name__))
            print("Cantidad: " + pastel_gourmet.cantidad_gourmet + "\n" +
                  "Precio: " + pastel_gourmet.precio_gourmet + "\n" +
                  "Sabor: " + pastel_gourmet.sabor_gourmet)

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
                "3- Pastel Helado. Introduzca la cantidad, precio y sabor. En dicho orden")

            pastel_helado = PastelHelado(input(), input(), input())
            mi_lista.append(pastel_helado)

            print("\nLa cantidad de pedidos en el carrito es de: " +
                  str(len(mi_lista)))
            print("Se agrego un pastel al carrito con las siguientes caracteristicas: ")
            print("Tipo de pastel: " +
                  str(type(mi_lista[len(mi_lista)-1]).__name__))
            # print(type(mi_lista[len(mi_lista)-1]).__name__)
            print("Cantidad: " + pastel_helado.cantidad_helado + "\n" +
                  "Precio: " + pastel_helado.precio_helado + "\n" + "Sabor: " + pastel_helado.sabor_helado + "\n")

        elif producto == "4":
            print("Se ha finalizado la compra \n")

            s_n = input(
                "Para proceder a realizar la factura, desea cargar los datos del cliente? \n S o N")
            if s_n.lower() == "s":
                # llamar a una funcion que cargue al cliente con sus productos y sus datos tributarios
                clientedatos = self.carga_datos_cliente(s_n)
                self.relizar_factura(clientedatos)

                quit()
            else:

                #clientedatos = self.carga_datos_cliente(s_n)
                self.relizar_factura(self.carga_datos_cliente(s_n))

                # llamar a una funcion que imprima la factura con los datos anonimos y termina el programa
                quit()

        elif producto == "5":
            print("\nGracias por usar FactuPy\n")
            quit()

    def menu_principal(self):
        choice = input(
            " Introduzca una opcion \n 1- Agregar productos \n 2- Salir \n")

        while choice != "2":
            self.agregar_nuevo_producto()
        else:
            print("\nGracias por usar FactuPy\n")

    def carga_datos_cliente(self, tipofactura):
        self.tipofactura = tipofactura
        if tipofactura == "s":
            print(
                "Introduzca los datos del cliente. \n Cedula, nombre y apellido, dirección. En ese orden")
            cliente = Cliente(input(), input(), input())
            return cliente

        else:
            cliente = Cliente(123456789, "Sin nombre", "Sin direccion")
            return cliente

    def relizar_factura(self, clien):

        self.clien = clien
        iva = 11
        total = 0
        iva_total = 0

        print("\n\n\n")
        print("-------" + empresa.nombre + "-------\n")
        print("-------" + empresa.dirección + "-------\n")
        print("\n")

        print("CANTIDAD------PRODUCTO/SABOR-------PRECIO------- IVA 10%------- SUBTOTAL ")

        for x in range(len(mi_lista)):

            if str(type(mi_lista[x]).__name__) == "PastelGourmet":

                calculo_iva = int(mi_lista[x].precio_gourmet)/iva
                subtotal = int(mi_lista[x].cantidad_gourmet) * \
                    int(mi_lista[x].precio_gourmet)
                total += subtotal

                print(str(mi_lista[x].cantidad_gourmet) + "---Pastel Gourmet/" + str(mi_lista[x].sabor_gourmet) +
                      "---" + str(mi_lista[x].precio_gourmet) +
                      "---" + str(math.floor(calculo_iva)) +
                      "---" + str(subtotal))

            elif str(type(mi_lista[x]).__name__) == "PastelHelado":

                calculo_iva = int(mi_lista[x].precio_helado)/iva
                subtotal = int(mi_lista[x].cantidad_helado) * \
                    int(mi_lista[x].precio_helado)
                total += subtotal

                print(str(mi_lista[x].cantidad_helado) + "---Pastel Helado/" + str(mi_lista[x].sabor_helado) +
                      "---" + str(mi_lista[x].precio_helado) +
                      "---" + str(math.floor(calculo_iva)) +
                      "---" + str(subtotal))
                print("\n")

            # elif str(type(mi_lista[x]).__name__) == "PastelHelado":
            #     pass
        print("\nDESCUENTO: \n" + "IVA 10%: " +
              str(math.floor(total/iva)) + "\nTOTAL: " + str(total) + " guaranies")
        print("\nLocalidad: Sucursal Asuncion\n" + "Cliente: " + clien.nombre + "\n" +
              "RUC: " + str(clien.cedula) + "\n" + "Dirección: " + clien.direccion + "\n")
