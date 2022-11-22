from libros import consultarLibro, ingresarLibro, eliminarLibro, modificarLibro

menu = 0
subOpciones = ''


def gestion_cliente(subOpciones):
    subOpciones = input(
        'Gestión del cliente \n A.Alta Cliente \n C.Consulta estado del cliente \n M.Modificar teléfono o dirección del cliente \n E.Eliminar cliente \n V.Volver al menú anterior \n'
    )
    subOpciones = subOpciones.upper()
    if subOpciones == 'A':
        print('ALTA CLIENTE')
    elif subOpciones == 'C':
        print('CONSULTA ESTADO DEL CLIENTE')
    elif subOpciones == 'M':
        print('MODIFICAR TELEFONO O DIRECCION DEL CLIENTE')
    elif subOpciones == 'E':
        print('ELIMINAR CLIENTE')
    elif subOpciones == 'V':
        menu_principal(menu)
    else:
        print('\nSeleccione opción valida \n')
        gestion_cliente(subOpciones)

def submenuConsultarLibro():
    subOpciones = input('Consultar por: \nA. Autor \nT. Título \nI. ISBN')
    subOpciones = subOpciones.upper()

    if subOpciones == 'A':
        consulta = input("Escriba el nombre del autor:")
        resultado=consultarLibro('autor', consulta)
        print(resultado)
        return
    elif subOpciones == 'T':
        consulta = input("Escriba el título del libro:")
        consultarLibro('titulo', consulta)
    elif subOpciones == 'I':
        consultarLibro('ISBN', consulta)
    else:
        print('\nSeleccione opción valida \n')
        gestion_libro(subOpciones)

def submenuAltaLibro():
    autor = input("Ingrese el autor")
    titulo = input("Ingrese el título")
    isbn = input("Ingrese el ISBN")
    respuesta=ingresarLibro(autor, titulo, isbn)
    print(respuesta)
    return

def submenuEliminarLibro():
    isbn = input("Ingrese el ISBN.")
    respuesta=eliminarLibro(isbn)
    print(respuesta)
    return

def submenuModificarLibro():
    isbn=input("Ingrese el ISBN.")
    respuesta=modificarLibro(isbn)
    print(respuesta)
    return

def gestion_libro(subOpciones):
    subOpciones = input(
        'Gestión de Libro \n A.Alta Libro \n C.Consultar Libro \n M.Modificar Libro \n E.Eliminar Libro \n V.Volver al menú anterior \n'
    )
    subOpciones = subOpciones.upper()
    if subOpciones=='A':
        submenuAltaLibro()
        return
    if subOpciones == 'C':
        submenuConsultarLibro()
        return
    elif subOpciones=='M':
        submenuModificarLibro()
        return
    elif subOpciones=='E':
        submenuEliminarLibro()
        return
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
