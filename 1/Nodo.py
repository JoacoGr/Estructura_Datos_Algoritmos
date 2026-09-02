class nodo:
    __comienzo: int
    __sig = None
    
    def __init__(self, otro):
        self.__comienzo = otro
        self.__sig = None
        
    def get_item(self):
        return(self.__comienzo)
    
    def cargar_item(self, otro):
        self.__comienzo = otro
    
    def set_sig(self, otro):
        self.__sig =  otro
        
    def get_sig(self):
        return self.__sig
    
    