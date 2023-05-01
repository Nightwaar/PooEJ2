from clase import Viajero,op1,op2,op3
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('1: Consultar cantidad de millas', accion1),
        '2': ('2: Acumular millas', accion2),
        '3': ('3: Canjear millas', accion3),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('Has elegido la opción 1')
    op1()


def accion2():
    print('Has elegido la opción 2')
    op2()


def accion3():
    print('Has elegido la opción 3')
    op3()


def salir():
    print('Saliendo')