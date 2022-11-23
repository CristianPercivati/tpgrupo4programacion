from libros import consultarLibro, ingresarLibro, eliminarLibro, modificarLibro
from clientes import consultarCliente, eliminarCliente, modificarCliente, ingresarCliente

menu = 0
subOpciones = ''

def submenuConsultarCliente():
    tabla = "clientes"
    subOpciones = input(
        'Consultar por: \nN. Nombre \nT. Teléfono \nA. Dirección\nD. DNI\nSelección: ')
    subOpciones = subOpciones.upper()

    if subOpciones == 'N':
        consulta = input("Escriba el nombre (o parte del nombre) del cliente:: ")
        resultado = consultarCliente('nombre', consulta)
        print(resultado)
        return
    elif subOpciones == 'T':
        consulta = input("Escriba el teléfono del cliente: ")
        resultado=consultarCliente('tel', consulta)
        print(resultado)
        return
    elif subOpciones == 'A':
        consulta = input("Escriba la dirección del cliente: ")
        resultado=consultarCliente('direccion', consulta)
        print(resultado)
        return
    elif subOpciones == 'D':
        consulta = input("Escriba el DNI del cliente: ")
        resultado=consultarCliente('dni', consulta)
        print(resultado)
        return
    else:
        print('\nSeleccione opción valida \n')
        gestion_cliente(subOpciones)

def submenuAltaCliente():
    dni = input("Ingrese el DNI: ")
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la direccion: ")
    respuesta = ingresarCliente(dni, nombre, telefono, direccion)
    print(respuesta)
    return

def submenuModificarCliente():
    dni = input("Ingrese el DNI: ")
    respuesta = modificarCliente(dni)
    print(respuesta)
    return

def submenuEliminarCliente():
    dni = input("Ingrese el DNI: ")
    respuesta = eliminarCliente(dni)
    print(respuesta)
    return

def gestion_cliente(subOpciones):
    subOpciones = input(
        'Gestión del cliente \n A.Alta Cliente \n C.Consulta estado del cliente \n M.Modificar teléfono o dirección del cliente \n E.Eliminar cliente \n V.Volver al menú anterior \n'
    )
    subOpciones = subOpciones.upper()
    if subOpciones == 'A':
        submenuAltaCliente()
        menu_principal(0)
    elif subOpciones == 'C':
        print('CONSULTA ESTADO DEL CLIENTE')
        submenuConsultarCliente()
        menu_principal(0)
    elif subOpciones == 'M':
        print('MODIFICAR TELEFONO O DIRECCION DEL CLIENTE')
        submenuModificarCliente()
        menu_principal(0)
    elif subOpciones == 'E':
        print('ELIMINAR CLIENTE')
        submenuEliminarCliente()
        menu_principal(0)
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_cliente(subOpciones)


def submenuConsultarLibro():
    tabla = "libros"
    subOpciones = input(
        'Consultar por: \nA. Autor \nT. Título \nI. ISBN\nSelección: ')
    subOpciones = subOpciones.upper()

    if subOpciones == 'A':
        consulta = input("Escriba el nombre del autor: ")
        resultado = consultarLibro('autor', consulta)
        print(resultado)
        return
    elif subOpciones == 'T':
        consulta = input("Escriba el título del libro: ")
        consultarLibro('titulo', consulta)
        return
    elif subOpciones == 'I':
        consulta = input("Escriba el ISBN: ")
        consultarLibro('ISBN', consulta)
        return
    else:
        print('\nSeleccione opción valida \n')
        gestion_libro(subOpciones)

def submenuAltaLibro():
    autor = input("Ingrese el autor: ")
    titulo = input("Ingrese el título: ")
    isbn = input("Ingrese el ISBN: ")
    respuesta = ingresarLibro(autor, titulo, isbn)
    print(respuesta)
    return

def submenuEliminarLibro():
    isbn = input("Ingrese el ISBN: ")
    respuesta = eliminarLibro(isbn)
    print(respuesta)
    return

def submenuModificarLibro():
    isbn = input("Ingrese el ISBN: ")
    respuesta = modificarLibro(isbn)
    print(respuesta)
    return


def gestion_libro(subOpciones):
    subOpciones = input(
        'Gestión de Libro \n A.Alta Libro \n C.Consultar Libro \n M.Modificar Libro \n E.Eliminar Libro \n V.Volver al menú anterior \n'
    )
    subOpciones = subOpciones.upper()
    if subOpciones == 'A':
        submenuAltaLibro()
        menu_principal(0)
    if subOpciones == 'C':
        submenuConsultarLibro()
        menu_principal(0)
    elif subOpciones == 'M':
        submenuModificarLibro()
        menu_principal(0)
    elif subOpciones == 'E':
        submenuEliminarLibro()
        menu_principal(0)
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_libro(subOpciones)


def menu_principal(menu):
    menu = int(
        input(
            'Menú Principal Biblioteca \n 0.Colsulta de disponibilidad \n 1.Prestamo de libro \n 2.Gestión del cliente \n 3.Gestión del libro \n'
        ))
    if menu == 0:
        print("Consultando disponibilidad")
    elif menu == 1:
        print('Prestamo de libro')
    elif menu == 2:
        gestion_cliente(subOpciones)
    elif menu == 3:
        gestion_libro(subOpciones)
        menu_principal(0)
    else:
        print('\nSeleccione opción valida \n')
        menu_principal(menu)
