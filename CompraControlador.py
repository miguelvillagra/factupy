

from InterfazPasteleria import InterfazPasteleria
from nucleo import *
import math
from RegistroClientes import *

####################################OBS#########################################
# Para que todas las opciones de agregar productos funcionen                    #
# es necesario que se ingresen los datos en el orden que salga en pantalla      #
#################################################################################

x= RegistroClientes()

mi_lista = []  # array en donde guardamos los pedidos a realizar
empresa = EmpresaGastronómica(
    "Ceci gross pastelería", "Mcal Lopez/José Vinuales")




class CompraControlador(object):

    def __init__(self):
        self.interfazPasteleria = InterfazPasteleria()

    def agregar_nuevo_producto(self):
        producto = input(
            "Agregar productos: \n 1-Pastel Gourmet \n 2-Pastel Economico \n 3-Pastel Helado \n 4-Finalizar compra \n 5-Salir \n")

        self.interfazPasteleria.agregar_producto(
            lambda: print("\nSe selecciono la opcion: " + producto))
        if int(producto) > 5 or int(producto) < 1:
            print("Debe seleccionar un número entre el 1 y el 5. Intentelo de nuevo.")

        #Aca valida que tipo de pedido que quiere agregar al carrito, con su sabor, precio y cantidad
        #El carrito funciona como un array mi_lista = [] en donde van los pedidos que pueden tener diferentes cantidades de pasteles

        elif producto == "1":

            print(
                "1- Pastel Gourmet. Introduzca la cantidad, precio y sabor. En ese orden:  \n ")

            # PastelGourmet(cantidad, precio, sabor)
            pastel_gourmet = PastelGourmet(input(), input(), input())
            mi_lista.append(pastel_gourmet)
            # print(type(mi_lista[0]).__name__)

            print("\nLa cantidad de pedidos en el carrito es de: " +
                  str(len(mi_lista)))
            print("Se agrego un pastel al carrito con las siguientes caracteristicas: ")
            print("Tipo de pastel: " +
                  str(type(mi_lista[len(mi_lista)-1]).__name__))
            print("Cantidad: " + pastel_gourmet.cantidad_gourmet + "\n" +
                  "Precio: " + pastel_gourmet.precio_gourmet + "\n" +
                  "Sabor: " + pastel_gourmet.sabor_gourmet + "\n")

        elif producto == "2":
            opcion2 = input(
                "2- Pastel Economico. Introduzca opcion 'p' para pastel pequeño o 'm' para pastel mediano\n")

            if (opcion2.lower()) == "p":
                print(
                    "2- Pastel economico pequeño . Introduzca sabor, precio y cantidad. En ese orden:  \n ")
                pastel_economico_pequeno = PastelEconomico(
                    PastelPequeño(input(), input()), input())
                mi_lista.append(pastel_economico_pequeno)

                print("\nLa cantidad de pedidos en el carrito es de: " +
                      str(len(mi_lista)))
                print(
                    "\nSe agrego un pastel al carrito con las siguientes caracteristicas: ")
                print("Tipo de pastel: " +
                      str(type(mi_lista[len(mi_lista)-1]).__name__))
                print("Tamaño: Pastel Pequeño ")
                print("Cantidad: " + str(pastel_economico_pequeno.cantidad_economico))
                print(
                    "Precio: " + str(pastel_economico_pequeno.tamanho_economico.precio_pequenho))
                print("Sabor: " +
                      pastel_economico_pequeno.tamanho_economico.sabor_pequenho + "\n")
            else:
                print(
                    "2- Pastel economico mediano . Introduzca sabor, precio y cantidad. En ese orden:  \n ")

                pastel_economico_mediano = PastelEconomico(
                    PastelMediano(input(), input()), input())
                mi_lista.append(pastel_economico_mediano)

                print("\nLa cantidad de pedidos en el carrito es de: " +
                      str(len(mi_lista)))
                print(
                    "\nSe agrego un pastel al carrito con las siguientes caracteristicas: ")
                print("Tipo de pastel: " +
                      str(type(mi_lista[len(mi_lista)-1]).__name__))
                print("Tamaño: Pastel Mediano ")
                print("Cantidad: " + str(pastel_economico_mediano.cantidad_economico))
                print(
                    "Precio: " + str(pastel_economico_mediano.tamanho_economico.precio_mediano))
                print("Sabor: " +
                      pastel_economico_mediano.tamanho_economico.sabor_mediano + "\n")

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
                "Para proceder a realizar la factura, desea cargar los datos del cliente? \n S o N\n")
            if s_n.lower() == "s":
                # llama a una funcion que cargua al cliente con sus productos y sus datos tributarios
                clientedatos = self.carga_datos_cliente(s_n)
                self.relizar_factura(clientedatos)

                quit()
            else:

                # llama a una funcion que imprime la factura con los datos anonimos y termina el programa
                self.relizar_factura(self.carga_datos_cliente(s_n))
                quit()

        elif producto == "5":
            print("\nGracias por usar FactuPy\n")
            quit()

    def menu_principal(self):
        
        #Aca inicia el programa y luego va a agregar_nuevo_producto si el usuario seleciona la opcion de 1- Agregar productos
        choice = input(
            " Introduzca una opcion \n 1- Agregar productos \n 2- Mostrar clientes registrados  \n 3- Salir \n")

        while choice == "1" or choice == "2":
            
            if choice =="1":
                self.agregar_nuevo_producto()
            else:
                
                print(x.mostrar())
                choice = "1"
               
        else:
            print("\nGracias por usar FactuPy\n")

    def carga_datos_cliente(self, tipofactura):
        #Si el usuario selecciona la opcion "s" se realiza el proceso de carga en la clase Cliente
        #para luego mandarlo a la funcion self.relizar_factura(clientedatos) y asi imprimir

        self.tipofactura = tipofactura
        if tipofactura == "s":
            print(
                "Introduzca los datos del cliente. \n Cedula, nombre y apellido, dirección. En ese orden")
            cliente = Cliente(input(), input(), input())
            s_n=input("Desea guardar al cliente en la base de datos?\n S o N\n")
            if s_n.lower() == "s":
                print("se guardo los datos del cliente")
                x.carga(cliente)
                x.mostrar()

            else:
                print("NO se guardo los datos del cliente")
            return cliente

        else:  # Se cargar los datos de forma anonima si el usuario selecciona otra opcion distinta de "s"
            cliente = Cliente(123456789, "Sin nombre", "Sin direccion")
            return cliente

    def relizar_factura(self, clien):

        self.clien = clien
        iva = 11
        total = 0
        iva_total = 0
        factura = Factura("123", clien)

        #Datos de la empresa gastronomica que seran mostrados al principio de la factura
        print("\n\n\n")
        print("-------" + empresa.nombre + "-------\n")
        print("-------" + empresa.dirección + "-------\n")
        print("\nFACTURA NRO: " + factura.numero)

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

            elif str(type(mi_lista[x]).__name__) == "PastelEconomico":

                if str(type(mi_lista[x].tamanho_economico).__name__) == "PastelPequeño":

                    calculo_iva = int(
                        mi_lista[x].tamanho_economico.precio_pequenho)/iva
                    subtotal = int(mi_lista[x].cantidad_economico) * \
                        int(mi_lista[x].tamanho_economico.precio_pequenho)
                    total += subtotal

                    print(str(mi_lista[x].cantidad_economico) + "---Pastel Economico Pequeño/" + str(mi_lista[x].tamanho_economico.sabor_pequenho) +
                          "---" + str(mi_lista[x].tamanho_economico.precio_pequenho) +
                          "---" + str(math.floor(calculo_iva)) +
                          "---" + str(subtotal))

                else:
                    calculo_iva = int(
                        mi_lista[x].tamanho_economico.precio_mediano)/iva
                    subtotal = int(mi_lista[x].cantidad_economico) * \
                        int(mi_lista[x].tamanho_economico.precio_mediano)
                    total += subtotal

                    print(str(mi_lista[x].cantidad_economico) + "---Pastel Economico Mediano/" + str(mi_lista[x].tamanho_economico.sabor_mediano) +
                          "---" + str(mi_lista[x].tamanho_economico.precio_mediano) +
                          "---" + str(math.floor(calculo_iva)) +
                          "---" + str(subtotal))
        #Aca se muestra el total a pagar y datos del cliente que fueron cargados en carga_datos_cliente1
        print("\nDESCUENTO: \n" + "IVA 10%: " +
              str(math.floor(total/iva)) + "\nTOTAL: " + str(total) + " guaranies")
        print("\nLocalidad: Sucursal Asuncion\n" + "Cliente: " + clien.nombre + "\n" +
              "RUC: " + str(clien.cedula) + "\n" + "Dirección: " + clien.direccion + "\n")
