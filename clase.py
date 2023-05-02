class Viajero:
    __NumeroViajero= ''
    __DNI= ''
    __nombre = ''
    __apellido= ''
    __millasacumuladas=0
    def __init__(self,NumeroViajero='',DNI='',nombre='',apellido='',millasacumuladas=0):
        self.__NumeroViajero = NumeroViajero
        self.__DNI = DNI
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__millasacumuladas = int(millasacumuladas) 
    def accion1(self):
        return self.__millasacumuladas
    def accion2(self,millas=0):
        self.__millasacumuladas = self.__millasacumuladas + millas
        print('La cantidad es {}'.format(self.__millasacumuladas))
        return 
    def accion3(self,millascanjear):
        if millascanjear <= self.__millasacumuladas:
            self.__millasacumuladas = self.__millasacumuladas - millascanjear
            print('Millas canjeadas')
        else: 
            print('No se puede canjear')
        return
    def mostrar(self):
            print('El numero de viajero es:{}'.format(self.__NumeroViajero))
            print('El DNI es:{}'.format(self.__DNI))
            print('El nombre es: {}'.format(self.__nombre))
            print('El apellido es:{}'.format(self.__apellido))
            print('Las millas acumuladas son: {}'.format(self.__millasacumuladas))
    def verifnum(self,numero):
        if self.__NumeroViajero == numero:
            return True
    def ingreso(lista):
        numviajero = input("Ingrese un numero de viajero:")
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                print(lista[i])
                return i