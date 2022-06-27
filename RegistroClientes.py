
import pickle
from CompraControlador import *




class RegistroClientes(object):

    

    def carga(self, cliente):
        array1=[]
        self.cliente = cliente
        
    

        #Primero abrimos para ver que hay dentro y guardar todo lo que haya antes
        pickle_in = open('listaclientes.pickle', 'rb')
        array1 = pickle.load(pickle_in)
        array1.append(cliente)
        pickle_in.close()


        #Ahora guaramos el array con el ultimo cliente agregado 

        pickle_out = open('listaclientes.pickle', 'wb')
        pickle.dump(array1, pickle_out)
        pickle_out.close()

        print( "Se han cargado los datos del cliente " + cliente.nombre + "\n" + "en la base de datos")

    def mostrar(self):
        array2= []
        pickle_in = open('listaclientes.pickle', 'rb')
        array2 = pickle.load(pickle_in)

        print(" \n********Clientes registrados:********\n")
        for x in range(len(array2)):
            print("Cliente"+str(x+1)+ ": " + array2[x].nombre + "\n" +
              "RUC: " + str(array2[x].cedula) + "\n" + "Dirección: " + array2[x].direccion + "\n")


# x= RegistroClientes
# x.mostrar()        

