class nodo:
    __item: object
    __sig: object

    def __init__(self, otro):
        self.__item = otro
        self.__sig = None

    def get_item(self):
        return self.__item

    def set_item(self, otro):
        self.__item = otro

    def get_sig(self):
        return self.__sig

    def set_sig(self, sig):
        self.__sig = sig

    def __str__(self):
        return f'{self.__item}'

    