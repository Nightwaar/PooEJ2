from clase import Viajero
import csv
if __name__ == '__main__' :
    #viajero = Viajero(1,1,'marcos','molina',111)
    listaviajeros= []
    archivo = open('viajeros.csv')
    reader= csv.reader(archivo,delimiter=',')
    for fila in reader:
        #print(fila)
        listaviajeros.append(Viajero(fila[0],fila[1],fila[2],fila[3],fila[4]))
    for i in range(len(listaviajeros)):
        listaviajeros[i].mostrar()
    numviaj = input('Ingrese su numero de viajero:')
    Viajero.ingreso(listaviajeros,numviaj)