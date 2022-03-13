from graphviz import Digraph, Graph
import time


class Pizzas:
    def __init__(self,nombre = None, direccion = None, telefono = None, cantidad = None, ingredientes = None, hora = None,codigo = None,tiempo_espera =None ,siguiente = None):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.cantidad = cantidad
        self.ingredientes = ingredientes
        self.hora = hora
        self.codigo = codigo
        self.tiempo_espera = tiempo_espera
        self.siguiente = siguiente

class Ingredientes:
    def __init__(self):
        self.raiz = Pizzas()
        self.ultimo = Pizzas()

    def insertar(self, nuevapizza):
        if self.raiz.nombre == None:
            self.raiz = nuevapizza
            self.ultimo = nuevapizza
        
        elif self.raiz.siguiente == None:
            self.raiz.siguiente = nuevapizza
            self.ultimo = nuevapizza
        else:
            self.ultimo.siguiente = nuevapizza
            self.ultimo = nuevapizza

    def eliminar(self, codigo):
        aux = self.raiz
        ant = None
        while aux != None:
            if aux.codigo == codigo:
                if ant == None:
                    self.raiz = aux.siguiente
                else:
                    ant.siguiente = aux.siguiente
                return True
            ant = aux
            aux = aux.siguiente
        return False


    def imprimir(self):
        aux = self.raiz
        while aux != None:
            print(aux.nombre + " " + aux.direccion + " " + aux.telefono + " " + aux.cantidad + " " + aux.ingredientes + " " + aux.hora + " " + aux.codigo + " " + aux.tiempo_espera)
            aux = aux.siguiente

    def despachar(self, codigo):
        aux = self.raiz
        espera = 0
        while aux != None:
            if aux.codigo == codigo:
                if espera == 0:
                    print("Pizza ingresada a las: "+aux.hora)
                    hora =  time.strftime("%X")
                    print("Pizza despachada a las: "+hora)
                    Ingredientes.eliminar(self, codigo)                
                    
                else:
                    print("Hay actualmente " + str(espera) + " pizzas en espera")
                    break
            else:
                espera = espera + 1
            aux = aux.siguiente
            

    def graficar(self):
        aux = self.raiz
        if aux.nombre == None:
            print("No hay pizzas")
            return
        else:
            x = ""
            dot = Digraph(filename='Grafica de pisos', format= 'png')

            while aux != None:
                x = x+'''<TD BGCOLOR="white"><FONT >'''+aux.nombre+"---"+str(aux.codigo)+"---"+aux.ingredientes+'''</FONT></TD>'''
                aux = aux.siguiente

            dot.node('tab',shape='plaintext', label='''<<TABLE CELLSPACING="0">
			
                <TR>'''+x+'''
                
                </TR>
                    </TABLE>>''')
            dot.view()





        

