class Viajero:
    __NumeroViajero= ''
    __DNI= ''
    __nombre = ''
    __apellido= ''
    __millasacumuladas=''
    def __init__(self,NumeroViajero='',DNI='',nombre='',apellido='',millasacumuladas=''):
        self.__NumeroViajero = NumeroViajero
        self.__DNI = DNI
        self.__nombre = nombre 
        self.__apellido = apellido 
        self.__millasacumuladas = millasacumuladas 
    def cantidadTotaldeMillas(self):
        return 'La cantidad total de millas es: {}'.format(self.__millascumuladas)
    def acumularmillas(self,millas):
        self.__millasacumuladas = self.__millasacumuladas + millas
    def canjearmillas(self,millascanjear):
        if millascanjear <= self.__millasacumuladas:
            print('Millas canjeadas')
        else: 
            return 'Error'
    def mostrar(self):
            print('El numero de viajero es:{}'.format(self.__NumeroViajero))
            print('El DNI es:{}'.format(self.__DNI))
            print('El nombre es: {}'.format(self.__nombre))
            print('El apellido es:{}'.format(self.__apellido))
            print('Las millas acumuladas son: {}'.format(self.__millasacumuladas))
    def verifnum(self,numero):
        if self.__NumeroViajero == numero:
            return True
    def ingreso(lista,numviajero):
        for i in range(len(lista)):
            if lista[i].verifnum(numviajero) == True:
                print(lista[i])
    def op1(self):
        print('La cantidad de millas es: {}'.format(self.__millasacumuladas))
    def op2(self):
        millas = input('Ingrese la cantidad de millas a acumular')
        self.__millasacumuladas = self.__millasacumuladas + millas
    def op3(self):
        millas = input('Ingrese la cantidad de millas a canjear')
        if self.__millasacumuladas >= millas:
            self.__millasacumuladas = self.__millasacumuladas - millas
        else:
            print('Error')
        return
