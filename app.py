from calendar import c
from pizza import Ingredientes, Pizzas
import time
import webbrowser as wb

a = Ingredientes()
codigo = 1

def opcion_1():
        global codigo  
        tiempo =0
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        cantidad = int(input("Ingrese la cantidad de pizzas de Don Cangrejo: "))

        for i in range(0,cantidad):            
            ingredientes = input("Ingrese el Ingrediente para la pizza "+str(i)+": ")
            if ingredientes == "Pepperoni":
                tiempo_espera = 3
                tiempo = tiempo + tiempo_espera
            elif ingredientes == "Salchicha":
                tiempo_espera = 4
                tiempo = tiempo + tiempo_espera
            elif ingredientes == "Carne":
                tiempo_espera = 10
                tiempo = tiempo + tiempo_espera
            elif ingredientes == "Queso":
                tiempo_espera = 5
                tiempo = tiempo + tiempo_espera
            elif ingredientes == "Piña":
                tiempo_espera = 2
                tiempo = tiempo + tiempo_espera
            hora =  time.strftime("%X")
            t1 = Pizzas(nombre, direccion, telefono, cantidad, ingredientes, hora,codigo,tiempo_espera)
            a.insertar(t1)
        print("Orden ingresada correctamente")
        print("Tu tiempo de espera es de: ",tiempo," minutos")
        codigo = codigo + 1
        print("***************************************************")
        a.graficar()
        menu()

def opcion_2():
    a.graficar()
    menu()

def opcion_3():
    print("***************************************************")
    cr = int(input("Ingrese el codigo de la orden que desea despachar: "))
    a.despachar(cr)
    a.graficar()
    menu()

def opcion_4():
    wb.open_new('CV Javier Girón.pdf')
    menu()

def menu():
    global codigo    

    print("***************************************************")
    print("*"+"     Bienvenido al Crustaceo cascarudo  "+"         *")
    print("*"+"           ¿Qué deseas hacer? "+"                   *")
    print("*"+" 1. Ingresar orden "+"                              *")
    print("*"+" 2. Mostrar ordenes ingresadas "+"                  *")
    print("*"+" 3. Despachar orden "+"                             *")
    print("*"+" 4. Mostrar datos del desarrollador "+"             *")
    print("*"+" 5. Salir "+"                                       *")
    print("***************************************************")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        opcion_1()      
               

            
    elif opcion == 2:
        opcion_2()
        menu()
    
    elif opcion == 3:
        opcion_3()
        menu()
    
    elif opcion == 4:
        opcion_4()
        menu()

    elif opcion == 5:
        print("Gracias por utilizar el programa")
        exit()

    
    else:
        print("Opcion no valida")
        menu()


if __name__ == "__main__":
        
   menu()