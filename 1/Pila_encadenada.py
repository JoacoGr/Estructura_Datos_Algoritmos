from Nodo import nodo
class pila:
    __cant:int
    __tope:nodo
    
    def __init__(self):
        self.__cant=0
        self.__tope = None
        
    def vacia(self):
        if self.__cant == 0:
            aux = True
        else: aux = False
        return aux
    
    def insertar(self, otro):
        Nodo = nodo(otro)
        Nodo.set_sig(self.__tope)
        self.__tope = Nodo
        self.__cant += 1        
        return Nodo.obtener_item()
    
    def suprimir(self):
        x = 0
        if self.vacia():
            print("La pila está vacia")
        else: 
            aux = self.__tope
            x = self.__tope.obteneritem()
            self.__tope = self.__tope.get_sig()
            self.__cant -= 1
            return(x)