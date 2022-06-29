from cytoolz import *
from functools import reduce

#Autor: Miguel Villagra/ miguel.villagra@fpuna.edu.py


#Pasteles que el cliente compra y que agrega a su carrito
carrito= [
    {"tipo": "Pastel Gourmet", "cantidad":3, "sabor":"chocolate", "precio":95000 },
    {"tipo": "Pastel Helado", "cantidad":2, "sabor":"vainilla", "precio":50000 },
    {"tipo": "Pastel Economico Pequeno", "cantidad":8, "sabor":"cafe", "precio":5000 }
]

#Acciones que se realizan al carrito para obtener algun resultado
def acciones(accion):
    
    def total_a_pagar():
        print("el total a pagar es de: "+str(reduce(lambda x, y: x+y, list(map(lambda data: ( data["cantidad"]*data["precio"]), carrito)))) + " guaranies")
        

    def total_cantitdad_items():
        print("total de items en el carrito: "+str(reduce(lambda x, y: x+y, list(map(lambda data: ( data["cantidad"]), carrito)))) + " pasteles")


    def total_por_items():
        print("Total a pagar por cada tipo de pastel: \n" +str(list(map(lambda data: (data["tipo"], data["cantidad"]*data["precio"]), carrito)) ))

    def sabores():
        print("los sabores elegidos fueron:\n" + str(list(map(lambda data: ( data["sabor"]), carrito))))

    acciones_dicc ={
        "total_pago": total_a_pagar,
        "total_cantidad": total_cantitdad_items,
        "pago_por_items": total_por_items,
        "todos_los_sabores": sabores
    }
    return acciones_dicc[accion]


#Resultados
a= acciones("total_pago")
a()

b= acciones("total_cantidad")
b()

c= acciones("pago_por_items")
c()

d= acciones("todos_los_sabores")
d()

