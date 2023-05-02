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
    numviaj=Viajero.ingreso(listaviajeros)
    print ("1. Consultar millas ")
    print ("2. Acumular ")
    print ("3. Canjear ")
    print ("4. Salir ")
    opc = int(input("Ingrese opcion :")) 
    while opc !=4:
        if opc == 1:
            print("La cantidad de millas es: {}".format(listaviajeros[numviaj].accion1()))
        elif opc == 2:
            millas= int(input("Ingrese cantidad de millas a acumular")) 
            listaviajeros[numviaj].accion2(millas)
        elif opc == 3:
            millasACanjear = int(input("Ingrese la cantidad de millas a canjear "))
            listaviajeros[numviaj].accion3(millasACanjear)
        elif opc == 4:
            print ("\n Gracias por ingresar ")
        opc = int(input("2Ingrese opcion "))